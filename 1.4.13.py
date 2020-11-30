import cv2
import numpy as np
from matplotlib import pyplot as plt

#01.
# img = cv2.imread('Sudoku_v2.jpg')
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# edges = cv2.Canny(gray,50,150,apertureSize = 3)
# cv2.imshow('image',edges)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
# lines = cv2.HoughLines(edges,1,np.pi/90,50)
# for i in range(45):
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


#02.
# img = cv2.imread('Sudoku.jpg')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# edges = cv2.Canny(gray, 50, 200, None, 3)
# minLineLength = 100
# maxLineGap = 10
# lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength, maxLineGap)
# for x1, y1, x2, y2 in lines[0]:
#     cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
#
# cv2.imwrite('houghlines5.jpg', img)
