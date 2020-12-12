import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('dsu.jpg',1)
rows,cols,ch = img.shape

pts1 = np.float32([[319,278],[760,315],[766,507],[322,538]])
pts2 = np.float32([[0,0],[441,0],[441,192],[0,192]])
M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img,M,(441,192))
plt.figure(figsize=(20,15))
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()