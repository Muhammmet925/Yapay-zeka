import numpy as np
import cv2
dizi3 = np.array([
    [[255,0,0],[0,255,0],[0,0,255]],
    [[0,0,0],[0,255,0],[255,255,255]],
                  ],dtype=np.uint8)


cv2.imshow("deneme",dizi3)
cv2.imwrite("deneme1.png",dizi3)
cv2.waitKey()