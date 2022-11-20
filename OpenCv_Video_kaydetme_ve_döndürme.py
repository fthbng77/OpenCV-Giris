import time
import cv2
import numpy as np

time.sleep(2)


def main():

    kamera=cv2.VideoCapture(0)#bilgisayar kamerasını kullancagımız icin 0 degerini giriyoruz.
    #video adını yazarsanız bilgisayarda kayıtlı olan bir videoyu çalıştıracaktır.
    fourcc= cv2.VideoWriter_fourcc(*"XVID")#format yeniliyebiliyoruz
    #kayitta dosya adı ,formatımızı yazıyoruz,alıcağımız fps i ve video boyutunu ayarlıyoruz.
    kayit = cv2.VideoWriter("kayit.avi",fourcc,30,(640,480))

    while True:
        ret,frame= kamera.read()#gelen veriyi oku.

        goruntu_cevir=cv2.flip(frame,0)#görüntüyü ters cebirmemize yarıyor.

        if ret == True:
            kayit.write(frame)#ret degeri görüntü almamıza yarıyor/write ile de kaydediyoruz.
            kayit.write(goruntu_cevir)#ters görüntüyü kaydeder.
            #q ya bastıgınızda kayıt işlemi biticek

        cv2.imshow("frame",frame)#görüntü göster.
        cv2.imshow("goruntu cevir",goruntu_cevir)
        #25 milisaniye de bir görüntüden çık
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    kamera.release()#kamera görüntüyü kes
    cv2.destroyAllWindows()#bütün pencereleri kapat.

if __name__ == "__main__":
    main()

