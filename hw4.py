import cv2
import numpy as np
from matplotlib import pyplot as plt

# img = cv2.imread('dsu4.jpg')
# rows,cols,ch = img.shape
# pts1 = np.float32([[235,457],[238,269],[569,231],[564,493]])
# pts2 = np.float32([[235,457],[235,270],[570,270],[570,447]])
#
# img = cv2.imread('a.png',1)
# rows,cols,ch = img.shape
# pts1 = np.float32([[215,1548],[282,486],[1038,493],[1010,1596]])
# pts2 = np.float32([[215,1548],[215,490],[1040,490],[1040,1548]])

img = cv2.imread('dsu5.jpg')
rows,cols,ch = img.shape
pts1 = np.float32([[578,336],[588,547],[755,375],[765,543]])
pts2 = np.float32([[578,330],[588,547],[755,336],[765,541]])
M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img,M,(cols,rows))
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()
M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img,M,(cols,rows))
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()
cv2.imshow('img', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()