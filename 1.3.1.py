import numpy as np
import cv2
from matplotlib import pyplot as plt

#1.3.1 Basic Operations on Images
#목표 : 픽셀 값에 액세스하고 수정
#이미지 속성에 액세스
#이미지 영역 (ROI) 설정
#이미지 분할 및 병합
#이 섹션의 거의 모든 작업은 주로 OpenCV가 아닌 Numpy와 관련이 있습니다. OpenCV로 더 최적화 된 코드를 작성하려면 Numpy에 대한 충분한 지식이 필요합니다.

#01. Accessing and Modifying pixel values
#행 및 열 좌표로 픽셀 값에 액세스 할 수 있습니다.
#img = cv2.imread('sky.jpg')
# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# px = img[100,100]
# print(px)
#
# for x in range(100):
#     for y in range(50):
#         img[100+y,100+x]=[0,0,0] #검정색
# cv2.imshow('image',img)
# k = cv2.waitKey(0)
# if k==27:
#     cv2.destroyAllWindows()
# #accessing only blue pixel
# blue = img[100,100,0]
# print(blue)
# #You can modify the pixel values the same way
# #Numpy는 빠른 배열 계산을 위해 최적화 된 라이브러리입니다. 따라서 각 픽셀에 액세스하기 만하면
# #값과 수정은 매우 느리므로 권장하지 않습니다.
# img[100,100]=[255,255,255] #해당 픽셀을 흰색으로 바꾸기
#
# print(img[100,100])
# #Numpy array의 item()함수는 개별적인 픽셀에 접근할 수 있지만, B,G,R 개별적으로 접근해야 합니다.
# #만약 (340,200) 위치의 픽셀값을 변경하려면, img.itemset()함수를 이용하면 되고, 이 역시 B,G,R 개별적인 값을 변경해주어야한다.
# #ex) B = img.item(340,200,0)
# #G = img.item(340,200,1)
# #img.item(340,200,2)
#
# #accessing RED value
# print(img.item(10,10,2)) #58
#
# #modifying RED value
# img.itemset((10,10,2),100)
# print(img.item(10,10,2)) #100으로 바뀜

#02. Accessing Image Properties
#이미지 속성에는 행, 열 및 채널 수, 이미지 데이터 유형, 픽셀 수 등이 포함됩니다.
#이미지의 모양은 img.shape에 의해 액세스됩니다. 행, 열 및 채널 수의 튜플을 반환합니다 (이미지가
#색깔)
#이미지가 회색조이면 반환 된 튜플에는 행과 열 수만 포함됩니다. 그래서 좋은 방법입니다
#로드 된 이미지가 회색조 또는 컬러 이미지인지 확인하십시오.
# print(img.shape)

#총 픽셀 수는 img.size로 액세스됩니다.
# print(img.size)

#이미지 데이터 유형은 img.dtype으로 가져옵니다.
#OpenCV-Python 코드에서 많은 오류가 발생하기 때문에 img.dtype은 디버깅하는 동안 매우 중요합니다.
#잘못된 데이터 유형으로 인해 발생합니다.
# print(img.dtype)

# sliced = img[280:340,330:390]
#
# img[273:333,100:160]=sliced

#03. Image ROI
# img = cv2.imread('sky.jpg')
# ball = img[280:340, 330:390]
# img[273:333, 100:160] = ball

#04. Splitting and Merging Image Channels
#이미지의 B, G, R 채널은 필요할 때 개별 평면으로 분할 할 수 있습니다. 그런 다음 개별 채널
#다시 병합하여 BGR 이미지를 다시 형성 할 수 있습니다. 다음을 통해 수행 할 수 있습니다.
#cv2.split ()은 (시간 측면에서) 비용이 많이 드는 작업이므로 필요한 경우에만 사용하십시오. Numpy 인덱싱
#훨씬 더 효율적이며 가능하면 사용해야합니다.
# img = cv2.imread('sky.jpg')
# # b,g,r = cv2.split(img)
# # img=cv2.merge((b,g,r))
# # b=img[:,:,0]
# # img[:,:,2] = 0

#05. Making Borders for Images (Padding)
# #borderType
# #-BORDER_CONSTANT:일정한 색상의 테두리를 추가합니다.
# #-BORDER_REFLECT:테두리 요소의 거울반사가 된다. fedcba|abcdefgh|hgfedcb
# #-BORDER_REFLECT_101 or BORDER_DEFAULT:위와 동일하지만, 약간의 변경 gfedcb|abcdefgh|gfedcba
# #-BORDER_REPLICATE:마지막 요소가 전체적으로 복제 aaaaaa|abcdefgh|hhhhhhh
# #BORDER_WRAP:cdefgh|abcdefgh|abcdefg 설명을 할수 없다.
# BLUE = [255,0,0]
#
# img1 = cv2.imread('open.jpeg')
#
# replicate = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REPLICATE)
# reflect = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT)
# reflect101 = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT_101)
# wrap = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_WRAP)
# constant= cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE)
#
# plt.figure(figsize=(20,15))
# plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
# plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
# plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
# plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
# plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
# plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')
#
# plt.show()