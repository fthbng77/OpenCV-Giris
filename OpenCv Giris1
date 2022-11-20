"""
Gırıs
Türkce kaynakların artması ve yeni baslayanlara yardımcı olmak icin yazıyorum. 
işletim sistemi olarak Ubuntu 20.04 kullanıyorum ama hangi windows kullanmanız da bir şey değiştirmeyecektir.
Kodları python kullanarak yazacağım.
"""
"""
Öncelikle OpenCV modülünü import edeceğim
Kodlamaya geçmeden önce bir resim kullanacağız o yüzden var olan bir resminizi kullanın ya yeni bir resim indirin.
bu resmi kod yazacağınız dosyaya aktarmanız size kolaylık açısından yarar sağlayacaktır.
"""
import cv2

# Sıklıkla kullancağımız bir modül var o da numpy el alışkanlığı olması açısından yazıyorum.
# as np olarak kısaltıyoruz. (çünkü sıklıkla öyle kullanılıyor.)

import numpy as np

#Bu kodları kullana bilmek için iki tane resim indirdim
#internetten indirebilirsiniz.
#resimleri pythonda okutabilmek için cv2.imread()'i kullanıyoruz
#ilk parametreye resmi giriyoruz, isteğe bağlı olarak ikinci bir parametre giriyoruz.
resim0 = cv2.imread("joker.jpg")

#ikinci parametreyi sıfır girdim ve resim gri oldu.
resim = cv2.imread("joker.jpg",0)
resim2 = cv2.imread("batman.jpeg",0)

#imwrite ile dosya yoluna bu değiştirdiğimiz resmi kaydede biliyoruz.
cv2.imwrite("joker_gri.jpg",resim)
cv2.imwrite("batman_grı.jpeg",resim2)

#cv2.imshow("pencere adini yazıyoruz",resmi kaydettigimiz degiskeni yaziyoruz.
cv2.imshow("joker resmi",resim2)

cv2.waitKey(0)

cv2.destroyAllWindows()
