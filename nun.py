# pip install opencv-python
import cv2
resim = cv2.imread("resimler/r2.png")
# resim numpy turu bir nesne
print(resim)
print(type(resim))
import numpy as np
dizi = np.array([150,150,150])
print(dizi)
print(type(dizi))
print(dizi.dtype)


dizi2 = np.array([150,150,150],dtype=np.uint8)
print(dizi2)
print(type(dizi2))
print(dizi2.dtype)


import cv2
cv2.imshow("deneme",dizi2)
cv2.imwrite("deneme1.png",dizi2)
cv2.waitKey()
import numpy as np
dizi2 = np.array([150,150,150],dtype=np.uint8)
dizi3 = np.array([[255,0,0],[0,255,0],[0,0,255]],dtype=np.uint8)
dizi3 = np.array([[[255,0,0],[0,255,0],[0,0,255]]],dtype=np.uint8)
print(dizi2)
print(type(dizi2))
print(dizi2.dtype)


import cv2
cv2.imshow("deneme",dizi3)
cv2.imwrite("deneme1.png",dizi3)
cv2.waitKey()

import numpy as np
import cv2
dizi3 = np.array([
    [[255,0,0],[0,255,0],[0,0,255]],
    [[0,0,0],[0,255,0],[255,255,255]],
                  ],dtype=np.uint8)


cv2.imshow("deneme",dizi3)
cv2.imwrite("deneme1.png",dizi3)
cv2.waitKey()