import cv2
import numpy as np
from matplotlib import pyplot as plt

#1.4.9
#01.
# im = cv2.imread('Djed.jpg')
# kernel = np.ones((5,5),np.uint8)
# imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
# imgray=255-imgray #배경 반전
# ret,thresh = cv2.threshold(imgray,48,255,cv2.THRESH_BINARY)
# closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
# contours,hierarchy = cv2.findContours(closing, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# img = cv2.drawContours(im, contours, -1, (0,255,0), 3)
# cv2.imshow('thresh',thresh)
# cv2.imshow('contours',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#02.
# im = cv2.imread('Canopic-Jar.jpg')
# kernel = np.ones((5,5),np.uint8)
# imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
# imgray=255-imgray #배경 반전
# ret,thresh = cv2.threshold(imgray,8,255,cv2.THRESH_BINARY) #덜 채워졌을 땐, 스레솔드값 바꿔보(8)
# # closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
# opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
# contours,hierarchy = cv2.findContours(opening, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# img = cv2.drawContours(im, contours, -1, (0,255,0), 3)
# cv2.imshow('thresh',thresh)
# cv2.imshow('img',img)
# cv2.imshow('opening',opening)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#03.
# im = cv2.imread('Important-ancient-Egyptian-symbols-and-meanings.jpg')
# kernel = np.ones((5,5),np.uint8)
# imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
# imgray=255-imgray #배경 반전
# contours,hierarchy = cv2.findContours(imgray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# img = cv2.drawContours(im, contours, -1, (0,255,0), 1)
# cv2.imshow('contours',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#04. Moments
# im = cv2.imread('ras.png')
# kernel = np.ones((5,5),np.uint8)
# imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
# imgray=255-imgray #배경 반전
# ret,thresh = cv2.threshold(imgray,8,255,cv2.THRESH_BINARY) #덜 채워졌을 땐, 스레솔드값 바꿔보기 (8)
# contours,hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# img = cv2.drawContours(im, contours, -1, (0,255,0), 3)
#
# cnt = contours[0]
# M = cv2.moments(cnt)
#
# #센터계산
# cx = int(M['m10']/M['m00'])
# cy = int(M['m01']/M['m00'])
# #면적계산
# area = cv2.contourArea(cnt)
# #둘레계산
# perimeter = cv2.arcLength(cnt,True)
#
# img = cv2.circle(img,(cx,cy),5,(0,0,255),-1)
# font = cv2.FONT_HERSHEY_SIMPLEX
# msg="A"+str(area)+"L"+str(perimeter)
# cv2.putText(img,msg, (cx,cy), font, 1,(32,32,32), 2, cv2.LINE_AA )
#
# cv2.imshow('thresh',thresh)
# cv2.imshow('contours',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#05. Bounding Rectangle
img = cv2.imread('hand.jpeg')
kernel = np.ones((5,5),np.uint8)
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgray=255-imgray #배경 반전
ret,thresh = cv2.threshold(imgray,8,255,cv2.THRESH_BINARY) #덜 채워졌을 땐, 스레솔드값 바꿔보기 (8)
contours,hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
contours,hierarchy = cv2.findContours(opening, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# img = cv2.drawContours(img, contours, -1, (0,255,0), 3)

cnt = contours[0]
M = cv2.moments(cnt)

#센터계산
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
#면적계산
area = cv2.contourArea(cnt)
#둘레계산
perimeter = cv2.arcLength(cnt,True)

# img = cv2.circle(img,(cx,cy),5,(0,0,255),-1)
# font = cv2.FONT_HERSHEY_SIMPLEX
# msg="A"+str(area)+"L"+str(perimeter)
# cv2.putText(img,msg, (cx,cy), font, 1,(32,32,32), 2, cv2.LINE_AA )

cnt = contours[0]
epsilon = 0.001*cv2.arcLength(cnt,True)
approx = cv2.approxPolyDP(cnt,epsilon,True)
# img = cv2.drawContours(img,[approx], -1, (0,0,255), 3)

#Straight Bounding Rectangle
hull = cv2.convexHull(approx)
img = cv2.drawContours(img,[hull], -1, (0,255,0), 3)

x,y,w,h = cv2.boundingRect(cnt)
img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

#Rotated Rectangle
rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
img = cv2.drawContours(img,[box],0,(0,0,255),2)

#Minimum Enclosing Circle
(x,y),radius = cv2.minEnclosingCircle(cnt)
center = (int(x),int(y))
radius = int(radius)
img = cv2.circle(img,center,radius,(0,255,0),2)

#Fitting an Ellipse
ellipse = cv2.fitEllipse(cnt)
img = cv2.ellipse(img,ellipse,(0,255,0),2)

#Fitting a Line
rows,cols = img.shape[:2]
[vx,vy,x,y] = cv2.fitLine(cnt, cv2.DIST_L2,0,0.01,0.01)
lefty = int((-x*vy/vx) + y)
righty = int(((cols-x)*vy/vx)+y)
img = cv2.line(img,(cols-1,righty),(0,lefty),(0,255,0),2)

cv2.imshow('opening',opening)
cv2.imshow('contours',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
