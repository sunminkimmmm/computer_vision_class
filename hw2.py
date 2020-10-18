import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.namedWindow('image')
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.createTrackbar('hue', 'image', 0, 360, nothing)
cap = cv2.VideoCapture('tracking1.avi')

while (1):
    hue = cv2.getTrackbarPos('hue', 'image')

    ret, frame = cap.read()
    if ret == True:
        # Convert BGR to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # define range of blue color in HSV
        lower_blue = np.array([hue - 20, 0, 0])
        upper_blue = np.array([hue + 20, 150, 150])

        # Threshold the HSV image to get only blue colors
        mask = cv2.inRange(hsv, lower_blue, upper_blue)

        # Bitwise-AND mask and original image
        res = cv2.bitwise_and(frame, frame, mask=mask)
        msg = "hue: " + str(hue)
        cv2.putText(frame, msg, (10, 50), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow('image', frame)
        cv2.imshow('mask', mask)
        cv2.imshow('res', res)
    k = cv2.waitKey(100) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
