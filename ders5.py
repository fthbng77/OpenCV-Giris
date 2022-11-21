import cv2
import numpy as np
"""Gürültü bir sinyal bir kanal üzerinde aktarılırken,
çevredeki etkenlerin altında oluşan istenmeyen değişimlerdir."""
kamera = cv2.VideoCapture(0)


sari_ton_alt= np.array([20,50,50])
sari_ton_üst= np.array([37,255,255])

while True:

    ret,frame = kamera.read()

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    mask_sari= cv2.inRange(hsv,sari_ton_alt,sari_ton_üst)

    sari_algılama = cv2.bitwise_and(frame,frame,mask=mask_sari)
    #smoothed 
    #Bir numpy array döndürecek bize 15 satırlık bir deger döndürecek.
    """
    Karnel nedir?
    bir piksel ve çevresindeki piksellerin uygun başka bir matris ile carpılmasına denir.
    Bu matrise karnel denir.
    """
    
    kernel = np.ones((15,15),dtype=  np.float32) /225 #bu genelde ezbere kullanılan bir kalıp.
    #
    
    smoothed=cv2.filter2D(sari_algılama,-1,kernel)#bitwise ve -1 degerleri sabit.

    #
    blur = cv2.GaussianBlur(sari_algılama,(15,15),0)
    #median filtre
    median_blur= cv2.medianBlur(sari_algılama,15)
    #lateral filtre
    cv2.imshow("medianBlur",median_blur)

    cv2.imshow("blur",blur)
    cv2.imshow("smoothed",smoothed)
    cv2.imshow("renk_algilama_sari(siyah-beyaz)",mask_sari)
    cv2.imshow("sarii algilama",sari_algılama)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

print(kernel)
kamera.release()
cv2.destroyAllWindows()