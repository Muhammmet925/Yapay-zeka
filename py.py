import numpy as np
import cv2

img = np.zeros((100, 100, 3), dtype=np.uint8)
img[0:33, :] = [0, 0, 255]   # Kırmızı
img[33:66, :] = [0, 255, 0]  # Yeşil
img[66:100, :] = [255, 0, 0] # Mavi

cv2.imwrite("demo.png", img)
