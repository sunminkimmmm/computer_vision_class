import cv2
import numpy as np
from matplotlib import pyplot as plt

#01.
# img1 = cv2.imread('toy_1.png', 0)
# img2 = cv2.imread('toy_2.png', 0)
# #gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# sift = cv2.SIFT_create()
# kp1, des1 = sift.detectAndCompute(img1,None)
# kp2, des2 = sift.detectAndCompute(img2,None)
# img1v=cv2.drawKeypoints(img1, kp1, img1)
# img2v=cv2.drawKeypoints(img2, kp2, img2, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
# plt.figure(figsize=(40,26))
# plt.subplot(121), plt.imshow(img1v,'gray')
# plt.subplot(122), plt.imshow(img2v,'gray')
# plt.show()

#02.
# img1 = cv2.imread('dsu5.jpg', 0)
# img2 = cv2.imread('dsu6.jpg', 0)
# # Initiate SIFT detector
# sift = cv2.SIFT_create()
# # find the keypoints and descriptors with SIFT
# kp1, des1 = sift.detectAndCompute(img1,None)
# kp2, des2 = sift.detectAndCompute(img2,None)
# # BFMatcher with default params
# bf = cv2.BFMatcher()
# matches = bf.knnMatch(des1,des2, k=2)
#
# # Apply ratio test
# good = []
# for m,n in matches:
#     if m.distance < 0.75*n.distance:
#         good.append([m])
# # cv2.drawMatchesKnn expects list of lists as matches.
# img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=2)
# plt.figure(figsize=(30,15))
# plt.imshow(img3),plt.show()

