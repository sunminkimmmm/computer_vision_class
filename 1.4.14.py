import cv2
import numpy as np
from matplotlib import pyplot as plt

#01.
# img = cv2.imread('logocv.png',0)
# img = cv2.medianBlur(img,5)
# cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
#
# circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,
#                            param1=50,param2=30,minRadius=0,maxRadius=0)
#
# circles = np.uint16(np.around(circles))
# for i in circles[0,:]:
#     # draw the outer circle
#     cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
#     # draw the center of the circle
#     cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
#
# cv2.imshow('detected circles', cimg)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#02.
# img = cv2.imread('book.jpg')
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# edges = cv2.Canny(gray,150,200,apertureSize = 3)
# cv2.imshow('image',edges)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
# lines = cv2.HoughLines(edges,1,np.pi/90,50)
# print(lines.shape)
#
# for i in range(12):
#     for rho,theta in lines[i]:
#         a = np.cos(theta)
#         b = np.sin(theta)
#         x0 = a*rho
#         y0 = b*rho
#         x1 = int(x0 + 1000*(-b))
#         y1 = int(y0 + 1000*(a))
#         x2 = int(x0 - 1000*(-b))
#         y2 = int(y0 - 1000*(a))
#         cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
# cv2.imwrite('bookoffice.jpg',img)

#03.

# def nothing(x):
#     pass
# img = cv2.imread('book.jpg')
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# edges = cv2.Canny(gray,50,150,apertureSize = 3)
#
#
# cv2.namedWindow('image')
# cv2.createTrackbar('threshold', 'image', 100, 500, nothing)
# cv2.createTrackbar('number', 'image', 1, 100, nothing)
# while(1):
#     k = cv2.waitKey(1) & 0xFF
#     if k == 27:
#         break
#     threshold = cv2.getTrackbarPos('threshold', 'image')
#     number = cv2.getTrackbarPos('number', 'image')
#     lines = cv2.HoughLines(edges, 1, np.pi/180, threshold)
#     img_rgb = cv2.imread('./img/a4.jpg')
#     numbers = number
#     if(lines.shape[0]<number):
#         numbers = lines.shape[0]
#     for i in range(numbers):
#         for rho,theta in lines[i]:
#             a = np.cos(theta)
#             b = np.sin(theta)
#             x0 = a*rho
#             y0 = b*rho
#             x1 = int(x0 + 1000*(-b))
#             y1 = int(y0 + 1000*(a))
#             x2 = int(x0 - 1000*(-b))
#             y2 = int(y0 - 1000*(a))
#             cv2.line(img_rgb,(x1,y1),(x2,y2),(0,0,255),2)
#     cv2.imshow('image',img_rgb)
# cv2.destroyAllWindows()
# minLineLength = 10
# maxLineGap = 10
# lines = cv2.HoughLinesP(edges,1,np.pi/180,1,minLineLength,maxLineGap)
# for i in range(10):
#     for x1,y1,x2,y2 in lines[i]:
#         cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
# cv2.imwrite('houghlines5.jpg',img)

#04.
# def nothing(x):
#     pass
# img_rgb = cv2.imread('book.jpg')
# gray = cv2.cvtColor(img_rgb,cv2.COLOR_BGR2GRAY)
# edges = cv2.Canny(gray,50,150,apertureSize = 3)
# cv2.namedWindow('image')
# cv2.createTrackbar('minLineLength', 'image', 10, 500, nothing)
# cv2.createTrackbar('maxLineGap', 'image', 1, 100, nothing)
# cv2.createTrackbar('number', 'image', 1, 100, nothing)
# while(1):
#     k = cv2.waitKey(1) & 0xFF
#     if k == 27:
#         break
#     minLineLength = cv2.getTrackbarPos('minLineLength', 'image')
#     maxLineGap = cv2.getTrackbarPos('maxLineGap', 'image')
#     number = cv2.getTrackbarPos('number', 'image')
#     lines = cv2.HoughLinesP(edges,1,np.pi/180,1,minLineLength,maxLineGap)
#     numbers = number
#     if(lines.shape[0]<number):
#         numbers = lines.shape[0]
#     for i in range(numbers):
#         for x1,y1,x2,y2 in lines[i]:
#             cv2.line(img_rgb,(x1,y1),(x2,y2),(0,255,0),2)
#     cv2.imshow('image',img_rgb)
# cv2.destroyAllWindows()