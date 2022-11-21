import cv2
import numpy as np


kamera = cv2.VideoCapture(0)

dusuk= np.array([85,50,50])#mavi renk icin
yuksek = np.array([130,255,255])

while True:
    ret,frame = kamera.read()

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    #filtreleme işlemi yapmak için cv2.inRange kullanıyoruz.

    mask = cv2.inRange(hsv,dusuk,yuksek)

    mavi_filtre= cv2.bitwise_and(frame,frame,mask=mask)

    karnel= np.ones((5,5),np.uint8)
    #erosionda siyah alanı silmeye çalışıyor
    erosion = cv2.erode(mask,karnel, iterations= 1)
    #diolationda beyaz alanı kaplamaya çalışıyor.
    diolation = cv2.dilate(mask,karnel, iterations=1)
    
    opening= cv2.morphologyEx(mask,cv2.MORPH_OPEN,karnel)

    closing = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,karnel)
    cv2.imshow("erosion",erosion)
    cv2.imshow("dilate",diolation)
    cv2.imshow("opening",opening)
    cv2.imshow("closing",closing)
    cv2.imshow("mask",mask)
    cv2.imshow("mavi_filtreleme",mavi_filtre)

    if cv2.waitKey(25)& 0xFF == ord('q'):
        break

kamera.release()
cv2.destroyAllWindows()