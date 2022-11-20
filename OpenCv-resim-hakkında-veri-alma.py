import cv2


resim= cv2.imread("batman.jpeg",0)
print(resim.item(50,50),0)#0mavi 1 yeşil 2 kırmızı değerini veriyor.


#print(resim.size)#kaç bitten oluştuğunu söyler
#print(resim.dtype)#hangi tipte yazıldığını söyler
#print(resim.shape)#resmin boyutlarını söyler.geniş*yükseklik*renk sıkalası


#cv2.imshow("batman",resim)

cv2.waitKey(0)
cv2.destroyAllWindows()
