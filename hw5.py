import numpy as np
import cv2
from matplotlib import pyplot as plt


img = cv2.imread('coin.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
blur = cv2.GaussianBlur(gray, (3,3), 0)

circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1.2, 30, None, 200)
if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        cv2.circle(img,(i[0], i[1]), i[2], (0, 255, 0), 2)
        cv2.circle(img, (i[0], i[1]), 2, (0,0,255), 5)

plt.figure(figsize=(20,15))
plt.subplot(121), plt.imshow(thresh,'a')
plt.subplot(122), plt.imshow(img,'b')
plt.show()