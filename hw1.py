import cv2
import numpy as np

# 초기값 지정
drawing = False
mode = 0
font = cv2.FONT_HERSHEY_SIMPLEX

ix, iy = -1, -1
cx, cy = -1, -1

# mouse callback function
def draw_circle(event, x, y, flags, param):
    global ix, iy, cx, cy, drawing, mode

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
        cx, cy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cx, cy = x, y

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cx, cy = x, y
def nothing(x):
    pass

img = cv2.imread('dsu5.jpg')
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)
cv2.createTrackbar('value', 'image', 0, 255, nothing)

while (1):
    img = cv2.imread('dsu5.jpg')
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode += 1
        if mode > 3:
            mode = 0
    elif k == 27:
        break
    # get current positions of four trackars
    value = cv2.getTrackbarPos('value', 'image')
    if ix != -1 and iy != -1:
        cv2.rectangle(img, (ix, iy), (cx, cy), (0, 255, 0), 0)

        if mode == 1:
            clip = img[iy:cy, ix:cx]
            clip[:, :, 1] = 0  # green
            clip[:, :, 2] = 0  # red

        elif mode == 2:
            clip = img[iy:cy, ix:cx]
            clip[:, :, 0] = 0  # blue
            clip[:, :, 2] = 0  # red

        elif mode == 3:
            clip = img[iy:cy, ix:cx]
            clip[:, :, 0] = 0  # blue
            clip[:, :, 1] = 0  # green

    msg = "Mouse position (" + str(ix) + "," + str(iy) + ") - (" + str(cx) + "," + str(cy) + ") - " + str(value)
    cv2.putText(img, msg, (10, 30), font, .6, (255, 255, 255), 1, cv2.LINE_AA)

    cv2.imshow('image', img)

cv2.destroyAllWindows()
