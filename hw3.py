import cv2
import numpy as np

img = cv2.imread('sIMG_8254.JPG')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
for i in range(1,17,2):
    blur = cv2.GaussianBlur(gray, (i, i), 0)
    ret,th = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    coin = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1.24, 30, None, 200)
    if coin is not None:
        coin = np.uint16(np.around(coin))
        for a in coin[0,:]:
            cv2.circle(img, (a[0], a[1]), a[2], (0, 255, 0), 2)
cv2.imshow('circle', img)
cv2.waitKey(0)
cv2.destroyAllWindows()