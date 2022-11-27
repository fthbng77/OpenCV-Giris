"""
Bu eğitimde, BGR ↔ Gri, BGR ↔ HSV vb. görüntüleri bir renk uzayından diğerine nasıl dönüştüreceğinizi öğreneceksiniz.
cv.cvtColor(), cv.inRange() fonksiyonlarını öğreneceğiz.

cv.cvtColor(input_image, flag) resim koyucaz ve flag yazılan yere de dönüştürmek istediğimiz türü yazıcaz.

HSV için ton aralığı [0,179], doygunluk aralığı [0,255] ve değer aralığı [0,255] şeklindedir.
HSV'de bir rengi temsil etmek, BGR renk uzayından daha kolaydır

"""

import cv2 as cv
import numpy as np
"""
bu islemle kac tane flag fonksiyonu oldugunu ogrenebiliriz.
flags = [i for i in dir(cv) if i.startswith('COLOR_')
         
print(flags)
"""

cap = cv.VideoCapture(0)

while(1):
    
    #bunun ile her kareyi alıyoruz.
    ret,frame= cap.read()

    #BGR yi HSV ye donustur. 
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    #hsv uzayındaki istediğimiz renk aralığını yazıyoruz.

    alt_sari = np.array([22, 100, 100])
    
    üst_sari = np.array([38, 255, 255])

    #araligi söyleyelim.
    mask = cv.inRange(hsv, alt_sari, üst_sari)

    res = cv.bitwise_and(frame,frame,mask=mask)

    cv.imshow('frame',frame)
    cv.imshow('mask',mask)
    cv.imshow('res',res)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break

cv.destroyAllWindows()
