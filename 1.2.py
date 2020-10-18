import numpy as np
import cv2
from matplotlib import pyplot as plt

#1.2.1.~5
# #01.이미지 읽기
# img = cv2.imread('mark.jpeg',0)
# #이미지 보
# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# #02.이미지 저장하기
# cv2.namedWindow('image', cv2.WINDOW_NORMAL)
# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows
# #이미지 저장하기
# cv2.imwrite('lena.png',img)

#03. 키보드
# img = cv2.imread('mark.jpeg',0)
# cv2.imshow('image',img)
# k=cv2.waitKey(0)
# if k == 27: #wait for ESC key to exit
#     cv2.destroyAllWindows()
# elif k == ord('s'): # wait for 's'key to save and exit
#     cv2.imwrite('lena.png', img)
#     cv2.destroyAllWindows()

#04. matplotlib
# img = cv2.imread('mark.jpeg',0)
# plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
# plt.xticks([]), plt.yticks([]) #to hide tick values on X and Y axis
# plt.show()

#05. 카메라이용
# cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
#
# while (cap.isOpened()):
#     ret, frame = cap.read()
#     if ret == True:
#         frame = cv2.flip(frame, 0)
#
#         # write the flipped frame
#         out.write(frame)
#
#         cv2.imshow('frame', frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#     else:
#         break
# # Release everyThing if job is finished
# cap.release()
# out.release()
# cv2.destroyAllWindows()

#06.도형그리기
#Create a blck image
# img = np.zeros((512,512,3), np.uint8)
#
# #Draw a dignal blue line with thickness of 5 px
# img = cv2.line(img,(0,0),(511,511),(255,0,0),5)
#
# #Drawing Rectangle
# img = cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
#
# #Drawing Circle
# img = cv2.circle(img,(447,63), 63, (0,0,255), -1)
#
# #Drawing Ellipse
# img = cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)
#
# #Drawing Polygon
# pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
# pts = pts.reshape((-1,1,2))
# img = cv2.polylines(img,[pts],True,(0,255,255))
#
# cv2.imshow("Drawing", img)
# k=cv2.waitKey(0) #키보드 눌림 대기
# if k == 27: #ESC키
#     cv2.destroyAllwindows();

#07. Simple Demo
#더블클릭시, 둥근 원 생
# events = [i for i in dir(cv2) if 'EVENT' in i]
# print(events)
# #mous callback function
# def draw_circle(event,x,y,flag,param):
#     if event == cv2.EVENT_LBUTTONDBLCLK:
#         cv2.circle(img, (x,y),100,(255,0,0),-1)
#
# #Create a black image, a window and bind the function to window
# img = np.zeros((512,512,3), np.uint8)
# cv2.namedWindow('image')
# cv2.setMouseCallback('image', draw_circle)
#
# while(1):
#     cv2.imshow('image', img)
#     if cv2.waitKey(20) & 0xFF == 27:
#         break
# cv2.destroyAllWindows()김

#08. More Advanced Demo
#여기에서 직사각형 또는 원을 그립니다
#그림판 응용 프로그램 에서처럼 마우스를 드래그합니다. 따라서 마우스 콜백 함수는 두 부분으로 구성
# drawing = False  # true if mouse is pressed
# mode = True  # if True, draw rectangle, Press 'm' to toggle to curve
# ix, iy = -1, -1
#
#
# # mouse callback function
# def draw_circle(event, x, y, flags, param):
#     global ix, iy, drawing, mode
#
#     if event == cv2.EVENT_LBUTTONDOWN:
#         drawing = True
#         ix, iy = x, y
#     elif event == cv2.EVENT_MOUSEMOVE:
#         if drawing == True:
#             if mode == True:
#                 cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
#             else:
#                 cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
#     elif event == cv2.EVENT_LBUTTONUP:
#         drawing = False
#         if mode == True:
#             cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
#         else:
#             cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
#
#
# img = np.zeros((512, 512, 3), np.uint8)
# cv2.namedWindow('image')
# cv2.setMouseCallback('image', draw_circle)
#
# while (1):
#     cv2.imshow('image', img)
#     k = cv2.waitKey(1) & 0xFF
#     if k == ord('m'):
#         mode = not mode
#     elif k == 27:
#         break
#
# cv2.destroyAllWindows()

#09. Code Demo
#지정한 색상을 보여주는 간단한 응용 프로그램을 만듭니다.
#색상과 세 개의 트랙 바를 사용하여 B, G, R 색상을 각각 지정합니다. 트랙 바와 그에 따라 창 색상을 슬라이드합니다.
#기본적으로 초기 색상은 검정색으로 설정
#트랙 바의 또 다른 중요한 용도는 버튼이나 스위치로 사용하는 것입니다. OpenCV는 기본적으로 버튼이 없습니다.
#기능. 따라서 트랙 바를 사용하여 이러한 기능을 얻을 수 있습니다. 우리 응용 프로그램에서 우리는 하나의 스위치를 만들었습니다.
#스위치가 켜져있을 때만 작동하는 응용 프로그램, 그렇지 않으면 화면이 항상 검은 색입니다.
# def nothing(x):
#     pass
#
#
# # Create a black image, a window
# img = np.zeros((300, 512, 3), np.uint8)
# cv2.namedWindow('image')
# cv2.moveWindow('image', 100, 100)
#
# # create trackbars for color change
# cv2.createTrackbar('R', 'image', 0, 255, nothing)
# cv2.createTrackbar('G', 'image', 0, 255, nothing)
# cv2.createTrackbar('B', 'image', 0, 255, nothing)
#
# # create switch for ON/OFF functionality
# switch = '0 : OFF \n1 : ON'
# cv2.createTrackbar(switch, 'image', 0, 1, nothing)
#
# while (1):
#     cv2.imshow('image', img)
#     k = cv2.waitKey(1) & 0xFF
#     if k == 27:
#         break
#     # get current positions of four trackbars
#     r = cv2.getTrackbarPos('R', 'image')#트랙바 이름, 해당 창이름, 기본값, 최대값, 콜백함수
#     g = cv2.getTrackbarPos('G', 'image')
#     b = cv2.getTrackbarPos('B', 'image')
#     s = cv2.getTrackbarPos(switch, 'image')
#
#     if s == 0:
#         img[:] = 0
#     else:
#         img[:] = [b, g, r]
#
# cv2.destroyAllWindows()
