import cv2
import numpy as np

#1.4.5
#1. Erosion
# img = cv2.imread('j.png',0)
# kernel = np.ones((5,5),np.uint8)
# erosion = cv2.erode(img,kernel,iterations = 1)
# cv2.imshow('img',img)
# cv2.imshow('erosion',erosion)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#2. Dliation
# img = cv2.imread('j.png',0)
# kernel = np.ones((5,5),np.uint8)
# dilation = cv2.dilate(img,kernel,iterations = 1)
# cv2.imshow('img',img)
# cv2.imshow('dilation',dilation)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#3. Opening
# img = cv2.imread('j.png',0)
# kernel = np.ones((5,5),np.uint8)
# opening = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
# cv2.imshow('img',img)
# cv2.imshow('opening',opening)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#4. Closiong
# img = cv2.imread('j.png',0)
# kernel = np.ones((5,5),np.uint8)
# closing = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
# cv2.imshow('img',img)
# cv2.imshow('closing',closing)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#5. Morphological Gradient
# img = cv2.imread('j.png',0)
# kernel = np.ones((5,5),np.uint8)
# gradient = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
# cv2.imshow('img',img)
# cv2.imshow('gradient',gradient)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#6. Top Hat
img = cv2.imread('j.png',0)
kernel = np.ones((5,5),np.uint8)
tophat = cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)
cv2.imshow('img',img)
cv2.imshow('tophat',tophat)
cv2.waitKey(0)
cv2.destroyAllWindows()