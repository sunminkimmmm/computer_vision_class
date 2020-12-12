
import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread('img1.jpg', 0)
img2 = cv2.imread('img2', 0)

sift = cv2.SIFT_create()

kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1,des2, k=2)

list = []
for m,n in matches:
    if m.distance < 0.70*n.distance:
        list.append([m])
img = cv2.drawMatchesKnn(img1,kp1,img2,kp2,list,None,flags=2)

plt.imshow(img),plt.show()