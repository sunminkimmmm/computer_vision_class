import cv2
import numpy as np
from matplotlib import pyplot as plt

#01. Scailing
# img = cv2.imread('sIMG_2164.jpg')
# resN = cv2.resize(img,None,fx=8, fy=4, interpolation = cv2.INTER_NEAREST)
# resC = cv2.resize(img,None,fx=8, fy=4, interpolation = cv2.INTER_CUBIC)
#
# cv2.imshow('img',img)
# cv2.imshow('resNimage',resN)
# cv2.imshow('resC image',resC)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#02. Translation
# img = cv2.imread('sIMG_2164.jpg',1)
# tx=100
# ty=150
# rows,cols,ch = img.shape
# M = np.float32([[1,0,tx],[0,1,ty]])
# dst = cv2.warpAffine(img,M,(cols,rows))
# dst=cv2.rectangle(dst,(0,0),(tx,ty),(0,255,0),-1)
# cv2.imshow('img',dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#03. Rotation
# img = cv2.imread('sIMG_2164.jpg',1)
# rows,cols,ch = img.shape
# cx=100
# cy=0
# theta=45
# M = cv2.getRotationMatrix2D((cy,cx),theta,1)
# dst = cv2.warpAffine(img,M,(cols,rows))
# dst = cv2.circle(dst,(cx,cy),10,(0,0,255),-1)
# cv2.imshow('img',dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#04. Affine Transformation
# img = cv2.imread('dsu4.jpg')
# rows,cols,ch = img.shape
# pts1 = np.float32([[235,457],[238,269],[569,231]])
# pts2 = np.float32([[235,457],[235,270],[570,270]])
# M = cv2.getAffineTransform(pts1,pts2)
# dst = cv2.warpAffine(img,M,(cols,rows))
# plt.subplot(121),plt.imshow(img),plt.title('Input')
# plt.subplot(122),plt.imshow(dst),plt.title('Output')
# plt.show()
#
# cv2.imshow('img', dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#05. PerspectiveTransform --> 중요, 카메라 캘리그레이션, 여러가지 응용이 많아서 이해 꼭 필
# img = cv2.imread('dsu4.jpg')
# rows,cols,ch = img.shape
# pts1 = np.float32([[235,457],[238,269],[569,231],[564,493]])
# pts2 = np.float32([[235,457],[235,270],[570,270],[570,447]])

# img = cv2.imread('a.png',1)
# rows,cols,ch = img.shape
# pts1 = np.float32([[215,1548],[282,486],[1038,493],[1010,1596]])
# pts2 = np.float32([[215,1548],[215,490],[1040,490],[1040,1548]])

# img = cv2.imread('dsu5.jpg')
# rows,cols,ch = img.shape
# pts1 = np.float32([[578,336],[588,547],[755,375],[765,543]])
# pts2 = np.float32([[578,330],[588,547],[755,336],[765,541]])
# M = cv2.getPerspectiveTransform(pts1,pts2)
# dst = cv2.warpPerspective(img,M,(cols,rows))
# plt.subplot(121),plt.imshow(img),plt.title('Input')
# plt.subplot(122),plt.imshow(dst),plt.title('Output')
# plt.show()
# M = cv2.getPerspectiveTransform(pts1,pts2)
# dst = cv2.warpPerspective(img,M,(cols,rows))
# plt.subplot(121),plt.imshow(img),plt.title('Input')
# plt.subplot(122),plt.imshow(dst),plt.title('Output')
# plt.show()
# cv2.imshow('img', dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
