# BGR renk araligindaki bir rengi HSV aralgiginda karsiligini bulma
import cv2 as cv

import numpy as np


alt_sari= np.uint8([[[25, 146, 190]]])
üst_sari= np.uint8([[[100, 180, 250]]])

hsa_alt = cv.cvtColor(alt_sari,cv.COLOR_BGR2HSV)
hsa_üst = cv.cvtColor(üst_sari,cv.COLOR_BGR2HSV)

print(hsa_alt)
print(hsa_üst)
