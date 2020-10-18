import numpy as np
import cv2
from matplotlib import pyplot as plt

#1.3.2  Arithmetic Operations on Images
#목표 : 더하기, 빼기, 비트 연산 등과 같은 이미지에 대한 몇 가지 산술 연산을 배웁니다.
#cv2.add (), cv2.addWeighted () 등의 함수를 학습합니다.

#01. Image Addition
#OpenCV 함수, cv2.add () 또는 단순히 numpy 연산, res = img1 + img2로 두 개의 이미지를 추가 할 수 있습니다.
#두 이미지는 깊이와 유형이 동일해야합니다. 그렇지 않으면 두 번째 이미지가 스칼라 값일 수 있습니다.
# x = np.uint8([250])
# y = np.uint8([10])
# print(cv2.add(x,y)) # 250 + 10 = 260 => 255, 255를 넘으면, 255가 출력되고, 255를 넘지 않으면, 더한 값이 출력된다.
# print(x+y) # 250 + 10 = 260%256 = 4

#02. Image Blending
#이것은 또한 이미지 추가이지만 이미지에 다른 가중치를 부여하여 혼합 또는 투명 함을 제공합니다. 이미지는 아래 방정식에 따라 추가됩니다.
#두 이미지의 크키가같아야한다.
# img1 = cv2.imread('open.jpeg')
# img2 = cv2.imread('open.jpeg')
#
# dst = cv2.addWeighted(img1,0.7,img2,0.3,0) #imgA * a(0.7) + imgB * b(0.3) + c(0)
#
# cv2.imshow('dst',dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#03. Bitwise Operations
#여기에는 비트 AND, OR, NOT 및 XOR 연산이 포함됩니다. 그것들의 일부를 추출하는 동안 매우 유용합니다.
#두 개의 이미지를 추가하면 색상이 바뀝니다. 블렌딩하면 투명 해져
#효과. 그러나 나는 그것이 불투명하기를 원합니다. 직사각형 영역이라면 지난 장에서했던 것처럼 ROI를 사용할 수 있습니다.
# # Load two images
# img1 = cv2.imread('mark.jpeg')
# img2 = cv2.imread('open.jpeg')
#
# # I want to put logo on top-left corner, So I create a ROI
# rows,cols,channels = img2.shape
# roi = img1[0:rows, 0:cols ]
#
# # Now create a mask of logo and create its inverse mask also
# img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
# #cv2.threshold(img,threshold_value,value,flag)
# #img : Grayscale 이미지
# #threshold_value:픽셀 문턱값 --> 따라서 여기선 검정부분이 투명하게
# #value : 픽셀 문턱값보다 클 때 적용되는 최대값
# #flag:문턱값 적용 방법 또는 스타일
# ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
# mask_inv = cv2.bitwise_not(mask)
#
# # Now black-out the area of logo in ROI
# img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
#
# # Take only region of logo from logo image.
# img2_fg = cv2.bitwise_and(img2,img2,mask = mask)
#
# # Put logo in ROI and modify the main image
# dst = cv2.add(img1_bg,img2_fg)
# img1[0:rows, 0:cols ] = dst
#
# cv2.imshow('res',img1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()