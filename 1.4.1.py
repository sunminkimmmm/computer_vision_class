import numpy as np
import cv2
from matplotlib import pyplot as plt

#1.4.1 Changing Colorspaces
#목표 :이 튜토리얼에서는 BGR ↔ Gray, BGR↔HSV과 같이 한 색 공간에서 다른 색 공간으로 이미지를 변환하는 방법을 배웁니다.
#그 외에도 비디오에서 색상 개체를 추출하는 응용 프로그램을 만들 것입니다
#cv2.cvtColor (), cv2.inRange () 등의 함수를 학습합니다.

#01. Changing Color-space
#OpenCV에서 사용할 수있는 150 가지 이상의 색 공간 변환 방법이 있습니다.
#가장 널리 사용되는 것은 BGR ↔ Gray, BGR ↔ HSV입니다.
#색상 변환을 위해 플래그가 결정하는 함수 cv2.cvtColor (input_image, flag)를 사용합니다.
#BGR → Gray 변환의 경우 cv2.COLOR_BGR2GRAY 플래그를 사용합니다.
#유사하게, BGR → HSV경우 cv2.COLOR_BGR2HSV 플래그를 사용합니다.

#02. Object Tracking
#이제 BGR 이미지를 HSV로 변환하는 방법을 알았으므로이를 사용하여 컬러 개체를 추출 할 수 있습니다.
#HSV에서는 RGB 색 공간보다 색을 나타내기 더 쉽습니다.
#우리의 응용 프로그램에서 우리는 파란색 개체를 추출하려고 시도 할 것입니다.

#1.비디오의 각 프레임 촬영
#2.BGR에서 HSV 색 공간으로 변환
#3.파란색 범위에 대해 HSV 이미지를 임계 값으로 설정
#4.이제 파란색 개체 만 추출하면 원하는 이미지에서 무엇이든 할 수 있습니다.
# cap = cv2.VideoCapture(0)
# while (1):
#     # Take each frame
#     _, frame = cap.read()
#
#     # Convert BGR to HSV
#     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#
#     # define range of blue color in HSV
#     lower_blue = np.array([110, 50, 50])
#     upper_blue = np.array([130, 255, 255])
#
#     # Threshold the HSV image to get only blue colors
#     mask = cv2.inRange(hsv, lower_blue, upper_blue)
#     # Bitwise-AND mask and original image
#     res = cv2.bitwise_and(frame, frame, mask=mask)
#
#     cv2.imshow('frame', frame)
#     cv2.imshow('mask', mask)
#     cv2.imshow('res', res)
#     k = cv2.waitKey(5) & 0xFF
#     if k == 27:
#         break
# cv2.destroyAllWindows()

##비디오 입력한 버전
# cap = cv2.VideoCapture('video.mp4')
# while(1):
#     # Take each frame
#     ret, frame = cap.read()
#     if ret == True:
#     # Convert BGR to HSV
#         hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#         # define range of blue color in HSV
#         lower_blue = np.array([110,50,50])
#         upper_blue = np.array([130,255,255])
#         # Threshold the HSV image to get only blue colors
#         mask = cv2.inRange(hsv, lower_blue, upper_blue)
#         # Bitwise-AND mask and original image
#         res = cv2.bitwise_and(frame,frame, mask= mask)
#         cv2.imshow('frame',frame)
#         cv2.imshow('mask',mask)
#         cv2.imshow('res',res)
#         k = cv2.waitKey(100) & 0xFF
#         if k == 27:
#             break
# cv2.destroyAllWindows()

##track bar 버전

def nothing(x):
    pass

cap = cv2.namedWindow('image')
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.createTrackbar('hue','image',0,360,nothing)
cap=cv2.VideoCapture('tracking1.avi')

while(1):
    #ge current positions of four trackbars
    #getTrackbarPos(trackbarname, winowname) -> 트랙바의 현재 위치를 리턴하는 함수
    hue = cv2.getTrackbarPos('hue','image')
    # Take each frame
    ret, frame = cap.read()
    if ret == True:
        # Convert BGR to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # define range of blue color in HSV
        lower_blue = np.array([hue-20,0,0])
        upper_blue = np.array([hue+20,150,150])
        # Threshold the HSV image to get only blue colors
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        # Bitwise-AND mask and original image
        res = cv2.bitwise_and(frame,frame, mask= mask)
        msg = "hue: "+ str(hue)
        cv2.putText(frame, msg,(10,50), font, 1,(255,255,255),2,cv2.LINE_AA)
        cv2.imshow('image',frame)
        cv2.imshow('mask',mask)
        cv2.imshow('res',res)
    k = cv2.waitKey(100) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()

