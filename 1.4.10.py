import cv2
import numpy as np
from matplotlib import pyplot as plt

#1.4.10 Histograms in OpenCV
#01.
# img = cv2.imread('beach-438500_1280.jpg',0)
# cv2.imshow('img',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
# hist = cv2.calcHist([img],[0],None,[256],[0,256])
# hist,bins = np.histogram(img.ravel(),256,[0,256])
# img = cv2.imread('beach-438500_1280.jpg',0)
# plt.hist(img.ravel(),256,[0,256]); plt.show()

#02.
# img = cv2.imread('beach-438500_1280.jpg')
# color = ('b','g','r')
# for i,col in enumerate(color):
#     histr = cv2.calcHist([img],[i],None,[256],[0,256])
#     plt.plot(histr,color = col)
#     plt.xlim([0,256])
# plt.show()

#03.
# img = cv2.imread('beach-438500_1280.jpg',0)
# # create a mask
# mask = np.zeros(img.shape[:2], np.uint8)
# mask[100:753, 100:1180] = 255
# masked_img = cv2.bitwise_and(img,img,mask = mask)
# # Calculate histogram with mask and without mask
# # Check third argument for mask
# hist_full = cv2.calcHist([img],[0],None,[256],[0,256])
# hist_mask = cv2.calcHist([img],[0],mask,[256],[0,256])
# # plt.figure(figsize=(15,15))
# plt.subplot(221), plt.imshow(img, 'gray')
# plt.subplot(222), plt.imshow(mask,'gray')
# plt.subplot(223), plt.imshow(masked_img, 'gray')
# plt.subplot(224), plt.plot(hist_full), plt.plot(hist_mask)
# plt.xlim([0,256])
# plt.show()

#04.
# img = cv2.imread('beach-438500_1280.jpg',0)
# hist,bins = np.histogram(img.flatten(),256,[0,256])
# cdf = hist.cumsum()
# cdf_normalized = cdf * hist.max()/ cdf.max()
# plt.plot(cdf_normalized, color = 'b')
# plt.hist(img.flatten(),256,[0,256], color = 'r')
# plt.xlim([0,256])
# plt.legend(('cdf','histogram'), loc = 'upper left')
# plt.show()
#
# cdf_m = np.ma.masked_equal(cdf,0)
# cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
# cdf = np.ma.filled(cdf_m,0).astype('uint8')
# img2 = cdf[img]
# plt.subplot(121), plt.imshow(img, 'gray')
# plt.subplot(122), plt.imshow(img2,'gray')
# plt.show()
#
# hist,bins = np.histogram(img.flatten(),256,[0,256])
# cdf = hist.cumsum()
# cdf_normalized = cdf * hist.max()/ cdf.max()
# plt.plot(cdf_normalized, color = 'b')
# plt.hist(img2.flatten(),256,[0,256], color = 'r')
# plt.xlim([0,256])
# plt.legend(('cdf','histogram'), loc = 'upper left')
# plt.show()

#05.
img = cv2.imread('beach-438500_1280.jpg',0)
equ = cv2.equalizeHist(img)
# plt.figure(figsize=(15,20))
plt.subplot(121), plt.imshow(img, 'gray')
plt.subplot(122), plt.imshow(equ,'gray')
plt.show()

res = np.hstack((img,equ)) #stacking images side-by-side
# cv2.imwrite('res.png',res)
cv2.imshow('img',res)
cv2.waitKey(0)
cv2.destroyAllWindows()