#chap1.4.4
#01. Smoothing
# img = cv2.imread('open.jpeg')
# kernel = np.ones((5,5),np.float32)/25
# dst = cv2.filter2D(img,-1,kernel)
# plt.subplot(121),plt.imshow(img),plt.title('Original')
# plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
# plt.xticks([]), plt.yticks([])
# plt.show()
#
# cv2.imshow('img', dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#lena kernal
# l=1
# kernel = np.array([[0,-1,0],[-1,4,-1],[0,-1,0]],np.float32)
# img = np.random.randint(10, size=(12,12))
# #img = np.ones((10,10),np.float32)
# h,w=img.shape
# dst = np.zeros((h,w),np.int)
# for i in range(l,h-l):
#     for j in range(l,w-l):
#         t=0
#         for p in range(-l,l+1):
#             for q in range(-l,l+1):
#                 t += kernel[p+l,q+l]*img[i+p,j+q]
#         dst[i,j]=t
# img = cv2.imread('lena.png', 0)
# h,w=img.shape
# dst = np.zeros((h-2*l,w-2*l),np.uint8)
# for i in range(l,h-l):
#     for j in range(l,w-l):
#         t=0
#         for p in range(-l,l+1):
#             for q in range(-l,l+1):
#                 t += kernel[p+l,q+l]*img[i+p,j+q]
#         dst[i-l,j-l]=t
# cv2.imshow('img',img)
# cv2.imshow('dst',dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#02. Averageing
# img = cv2.imread('open.jpeg')
# blur = cv2.blur(img,(5,5))
# plt.subplot(121),plt.imshow(img),plt.title('Original')
# plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
# plt.xticks([]), plt.yticks([])
# plt.show()

#02. Gaussian Filtering
# img = cv2.imread('open.jpeg')
# blur = cv2.GaussianBlur(img,(5,5))
# plt.subplot(121),plt.imshow(img),plt.title('Original')
# plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
# plt.xticks([]), plt.yticks([])
# plt.show()

# #03. Median Filtering
# img = cv2.imread('open.jpeg')
# median = cv2.medianBlur(img,(5,5))
# plt.subplot(121),plt.imshow(img),plt.title('Original')
# plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(median),plt.title('Blurred')
# plt.xticks([]), plt.yticks([])
# plt.show()

#04. Bilateral Filtering
# img = cv2.imread('open.jpeg')
# bilateral = cv2.bilateralFilter(img,(5,5))
# plt.subplot(121),plt.imshow(img),plt.title('Original')
# plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(bilateral),plt.title('Blurred')
# plt.xticks([]), plt.yticks([])
# plt.show()
