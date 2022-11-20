"""
Renk filtreleme yapacagız.
Bilgisayara hengi renklerişimize yarayacaksa onları secmesini söyleyecegiz kısaca
renklerle filtreleme yapmak için hsv mantıgını kullanacağız

-hsv de degere parlaklıga ve doygunluga göre goruntu olusuyor
-HSV degerlerini birbirinden ayırt etmek,
-BGR degerlerini birbirinden ayırt etmekten daha kolay oldugu için 
-HSV degerlerinden birbirini ayırt ediyoruz.
-ek olarak hsv renk uzayında renk seçiminin daha doğal olmasıdır. Geniş bir renk aralığı seçilip uygulama ışığa
daha az duyarlı hale getirilebildigi için HSV kullanıyoruz.
"""

import cv2
import numpy as np

kamera = cv2.VideoCapture(0)

dusuk = np.array([90,50,50])#Buradaki 90 degeri en dusuk mavi degeri oluyor
yuksek= np.array([130,255,255])#buradaki 130 degeri de en yuksek mavi degeri oluyor.
#50 ile 255 te minimum ve maximum doygunluk degerlerini alıyoruz

kirmizi_ton_alt= np.array([150,30,30])
kirmizi_ton_üst= np.array([185,255,255])
#Burada ana etkili deger H Hue degeridir.
#                         H  S  V
yesil_ton_alt= np.array([150,30,30])
yesil_ton_üst= np.array([185,255,255])

while True:
    #burada ret parametresi kameranın açık olup olmadıgını kontrol ediyor.
    ret,frame = kamera.read()
    
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)#goruntumuzu HSV uzayı döndürüyoruz.

    #maskeleme işlemini hsv uzayına göre yapıyoruz.
    mask = cv2.inRange(hsv,dusuk,yuksek)#bu aralıktaki degerleri beyaz kalanları siyah yapıyoruz.

    mask_kirmizi= cv2.inRange(hsv,kirmizi_ton_alt,kirmizi_ton_üst)

    mavi_resim= cv2.bitwise_and(frame,frame,mask = mask)

    kırmızı_algılama = cv2.bitwise_and(frame,frame,mask=mask_kirmizi)
    cv2.imshow("Burada Blue,Green ve Red doner frame",frame)

    cv2.imshow("HSV Burada Hue,Stration,Value degerleri doner",hsv)

    cv2.imshow("mask",mask)#burada mavi dısındaki renkler siyah gözükecektir.

    cv2.imshow("renk_algilama_mavi",mavi_resim)# mavi algılama

    cv2.imshow("renk_algilama_kirmizi(siyah-beyaz)",mask_kirmizi)
    cv2.imshow("kirmizi algilama",kırmızı_algılama)
    #aşağıda video 25 milisaniyede bir görüntüler alsın ve 
    # q ya bastıgımızda döngü kırılsın diyoruz. Bu şekilde biz diyene kadar döngü devam edicek.
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

kamera.relaese()
cv2.destroyAllWindows()

"""
Burada ek bir bilgi vereyim:(son_resimde kullanıyoruz.)
siyah ile bir rengi bitledigimiz zaman siyaha döner cünkü bit degeri sıfırdır
sıfırla carpma sonucu deger sıfır cıkar ve siyahın bit degeri sıfırdır.
beyazda da bit degeri 1 oldugu icin ne ile carparsak carptıgımız degeri alır.
"""

"""
Mantık olarak Filtreleme islemi bu sekilde 
Hsv de bir renk aralıgını kapsayan rengi alıyoruz doygunluk degerlerini ayarladıktan sonra
görüntü ararken o renk aralıgını görüyoruz.
renk sıkalalarını resim olarak bıraktım.
"""