import cv2
import numpy as np
from matplotlib import pyplot as plt

#01.
# filename = 'horse_1.bmp'
# #filename = './img/Raspberry_Pi.png'
# img = cv2.imread(filename)
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#
# gray = np.float32(gray)
# dst = cv2.cornerHarris(gray,2,3,0.04)
#
# dst = cv2.dilate(dst,None)
#
# img[dst>0.01*dst.max()]=[0,0,255]
# cv2.imshow('dst',img)
# if cv2.waitKey(0) & 0xff == 27:
#     cv2.destroyAllWindows()
# def nothing(x):
#     pass
#
# cv2.namedWindow('image')
# cv2.createTrackbar('threshold','image',10,1000,nothing)
# while(1):
#     k = cv2.waitKey(1) & 0xFF
#     if k == 27:
#         break
#     threshold = cv2.getTrackbarPos('threshold','image')
#     if (threshold <= 1):
#         threshold=1
#     img = cv2.imread(filename)
#     img[dst>1./threshold*dst.max()]=[0,0,255]
#     cv2.imshow('image',img)
# cv2.destroyAllWindows()

#02.
# # find Harris corners
# gray = np.float32(gray)
# dst = cv2.cornerHarris(gray,2,3,0.04)
# dst = cv2.dilate(dst,None)
# ret, dst = cv2.threshold(dst,0.01*dst.max(),255,0)
# dst = np.uint8(dst)
# # find centroids
# ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)
#
# # define the criteria to stop and refine the corners
# criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
# corners = cv2.cornerSubPix(gray,np.float32(centroids),(5,5),(-1,-1),criteria)
#
# # Now draw them
# res = np.hstack((centroids,corners))
# res = np.int0(res)
# img[res[:,1],res[:,0]]=[0,0,255]
# img[res[:,3],res[:,2]] = [0,255,0]
# print(res.shape)
#
# cv2.imshow('dst',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
# for i in range(res.shape[0]):
#     cv2.circle(img,(res[i,0],res[i,1]),2,(0,0,255),-1)
#     cv2.circle(img,(res[i,2],res[i,3]),3,(0,255,0),-1)
# cv2.imshow('dst',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()