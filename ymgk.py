import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d

def process_video(video_path, output_csv_path, display=False, frame_rate=30):
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print("Error: Could not open video.")
        return
    
    hinge_positions = []

    delay = int(1000 / frame_rate)

    while cap.isOpened():
        ret, frame = cap.read()
        
        if not ret:
            break
        
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        lower_blue = np.array([100, 150, 50])
        upper_blue = np.array([140, 255, 255])
        
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 50:  
                M = cv2.moments(contour)
                if M["m00"] != 0:
                    cX = int(M["m10"] / M["m00"])
                    cY = int(M["m01"] / M["m00"])
                    hinge_positions.append((cX, cY))
                    
                    if display:
                        cv2.drawContours(frame, [contour], -1, (0, 0, 0), 2)  
                        cv2.circle(frame, (cX, cY), 5, (0, 0, 0), -1)  
                        cv2.putText(frame, f"({cX}, {cY})", (cX - 20, cY - 20),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)  
        if display:
            cv2.imshow("Frame", frame)
            if cv2.waitKey(delay) & 0xFF == ord('q'):
                break
    
    cap.release()
    cv2.destroyAllWindows()
    
    df = pd.DataFrame(hinge_positions, columns=['X', 'Y'])
    df.to_csv(output_csv_path, index=False)
    print(f"Positions saved to {output_csv_path}")
    
    df['X_smooth'] = gaussian_filter1d(df['X'], sigma=2)
    df['Y_smooth'] = gaussian_filter1d(df['Y'], sigma=2)
    
    plt.figure(figsize=(10, 5))
    plt.plot(df['X_smooth'], df['Y_smooth'], color='blue', alpha=0.5, linewidth=1)
    plt.title('Hinge Positions Over Time (Smoothed)')
    plt.xlabel('X Position')
    plt.ylabel('Y Position')
    plt.show()

    plt.figure(figsize=(10, 5))
    plt.hist(df['X'], bins=30, color='blue', alpha=0.7)
    plt.title('Histogram of X Positions')
    plt.xlabel('X Position')
    plt.ylabel('Frequency')
    plt.show()

    plt.figure(figsize=(10, 5))
    plt.hist(df['Y'], bins=30, color='blue', alpha=0.7)
    plt.title('Histogram of Y Positions')
    plt.xlabel('Y Position')
    plt.ylabel('Frequency')
    plt.show()

video_path = input("Enter the video path: ")
output_csv_path = 'output.csv'
process_video(video_path, output_csv_path, display=True, frame_rate=30)
