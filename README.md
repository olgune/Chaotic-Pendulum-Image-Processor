# Chaotic Pendulum Image Processor
 Yazılım mühendisliği güncel konular dersi için yapılmış kaotik pendulum hareketlerini görüntü işleme ile kayıt eden program

## Program nasıl çalışıyor
Programın çalışması için programa bir video yüklenmeli ve bu yüklenen videodaki pendulumun hareketlerini(geçtiği pixellerin değerlerini) program görüntü işleme yöntemleriyle kayıt edip  bir csv dosyası oluşturur, 3 tane de grafik çıktısı verir. İlk çalıştığında video görüntü işlemenin yapılması için oynatılır ve daha sonra video işlendikten sonra grafikler gösterilir ve csv dosyası oluşturulur.

## Programın çalışması için gerekenler
Programın çalışması için bilgisayarınızda python bulunması gerekli, ayrıca programda kullanılan kütüphanelerin de bilgisayarınızda yüklü olması gerekli. Gerekli kütüphanelerin hepsini indirmek için bu kodu terminale yazın "pip install opencv-python numpy pandas matplotlib scipy".

## Program nasıl çalıştırılır
Program çalıştırıldığında videonun yolunu input olarak girilmesini isteyecek ve videonun yolu buraya tam olarak girilmeli, girilmez ise hata verir ve kapanır program. Girilen dosya yolunda ters eğik çizgi ("\") kullanılmamalı düz eğik çizgi ("/") kullanılmalı. Örnek video yolu "C:/Users/User/Desktop/Project/video.mp4". Program çalışırken durdurmak için konsolda ctrl + c kombinasyonuna tıklanarak kapatılabilir. Çıkan grafikleri kaydetmek vb. işlemler için butonlar grafik ekranında bulunuyor.
