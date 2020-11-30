import cv2
import numpy as np
from matplotlib import pyplot as plt


#1.4.7 Canny Edge Detection
#01.
# img = cv2.imread('sIMG_2177.jpg',0)
# #cv2.Canny(img,canny_low_thresh,canny_high_thresh)
# #argument 무엇인지 이해해야한다. 이미지에 따라 적절히 조절 필
# edges = cv2.Canny(img,100,200)
# plt.subplot(121),plt.imshow(img,cmap = 'gray')
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(edges,cmap = 'gray')
# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
# plt.show()

#1.4.8 Image Pyramids
#01. 이미지 줄이기
# img = cv2.imread('sIMG_2177.jpg')
# img1 = cv2.pyrDown(img)
# img2 = cv2.pyrDown(img1)
# edges = cv2.Canny(img, 100, 200)
# edges1 = cv2.Canny(img1, 100, 200)
# edges2 = cv2.Canny(img2, 100, 200)
# cv2.imshow('edges1',edges1)
# cv2.imshow('edges2',edges2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#02. 이미지 늘리기
# img = cv2.imread('sIMG_2177.jpg')
# img1 = cv2.pyrUp(img)
# img2 = cv2.pyrUp(img1)
# edges = cv2.Canny(img, 100, 200)
# edges1 = cv2.Canny(img1, 100, 200)
# edges2 = cv2.Canny(img2, 100, 200)
# cv2.imshow('edges1',edges1)
# cv2.imshow('edges2',edges2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#03.
# img = cv2.imread('sIMG_8253.JPG')
# imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# ret,thresh = cv2.threshold(imgray,127,255,0)
# image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX)
# img = cv2.drawContours(img, contours, -1, (0,255,0), 3)
# cv2.imshow('thresh',thresh)
# cv2.waitKey(0)
# cv2.destroyAllWindows()