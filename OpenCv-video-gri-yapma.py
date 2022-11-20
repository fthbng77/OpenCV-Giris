#numpy ve cv2 nodullerini import ediyoruz.
import cv2
import numpy as np

"""
kamera varilerini almak icin 
kamera = cv2.VideoCapture(0)
içeriye 0 yaparsak bilgisayar kamerasını kullanır
1 yaparsak usb ile bagladığımız kamerayı kullanır
"video adı" yaparsak bilgisayarda adını yazdıgımız bir video yu kullanırız

"""
kamera = cv2.VideoCapture(0)

"""
kameranin boyutlarını ayarlamak için 
kamera.set(3,boyut)3 genişliğini ayarlamamıza yarıyor.
kamera.set(4,boyut)4 uzunluğunu belirlememize yarıyor.
boyutları ayarlamak için bir fonksiyon oluşturmak istersek;
öncelikle videonun boyutlarını almamız gerekiyor,
kare.shape ile boyutlarını alabiliriz,
[0] index bize görüntünün yüksekliğini verir
[1] index ise bize genişliğini verir.
sonra bunları istediğimiz orada ayarlamak için çarpıyoruz. 
YA DA bir fonksiyon yazabiliriz.
"""
"""
öncelikle bilgisayardan gelen görüntünün boyutlarını ögrenmeliyiz
kare.shape[indexi 1 verirsek genisligi,0 verirsek uzunlugu verir] ile ögrenebiliriz
alttaki fonksiyon ile görüntü boyutunu istediğiniz gibi ayarlayabilirsiniz
"""
def boyut_ayarlama(kare,yuzde=75):
    genislik = int(kare.shape[1]* yuzde/100)
    yukseklik = int(kare.shape[0]* yuzde/100)
    boyut = (genislik,yukseklik)
    return cv2.resize(kare,boyut,interpolation= cv2.INTER_AREA)

def main():
  while True: #döngünün bir şartta bağlanmadan dönmesini istiyoruz.
    ret,kare = kamera.read()#kameradan gelen veriyi oku
    gri_yapma = cv2.cvtColor(kare,cv2.COLOR_BGR2GRAY)
    kare2 = boyut_ayarlama(kare2,20)#görüntünün boyutunu yüzde 20 ye ayarladım
    
    cv2.imshow("kare",kare)#kameradan gelen veriyi göster.
    cv2.imshow("kare2",kare2)
    #25 milisaniyede bir görüntü vermesini istedigimiz için 25 yazıyoruz siz farklı bir şey de yazabilirsiniz.
    #1000 milisaniye = 1 saniye
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break
      
     kamera.release()#kameradan gelen verileri durdur
     cv2.destroyAllWindows()#tüm pencereleri kapat

if __name__ == "__main__":#fonksiyonu çalıştırıyoruz.
  main():


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
