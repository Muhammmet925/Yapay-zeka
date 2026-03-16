# rastgele iki renkli resim oluşturma
import cv2, numpy as np


r1= np.full((200, 200, 3), [255,0,255], dtype=np.uint8)


print(r1.shape)
for a in range(r1.shape[0]):
    for b in range(r1.shape[1]):
        if a % 10 < 5 : r1[a,b]=[0,0,0]
        # if b % 10 < 5 : r1[a,b]=[255,255,255]
        # if a==b : r1[a,b]=[255,0,0]
        # if r1.shape[0]-a==b : r1[a,b]=[0,255,0]
        # if b<r1.shape[0]-a<b+7 : r1[a,b]=[0,0,255]


cv2.imshow("Resim", r1)


cv2.waitKey(0)
