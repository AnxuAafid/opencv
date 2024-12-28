import cv2
import numpy as np

path = "resources/img01.jpg"

img =cv2.imread(path)

kernel = np.ones((5,5),np.uint8)
#print(kernel)
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
imgblur = cv2.GaussianBlur(imgray,(7,7),0)
imgCanny =cv2.Canny(imgblur,50,100)
imgdilation =cv2.dilate(imgCanny,kernel,iterations=3)
imgerode = cv2.erode(imgdilation,kernel,iterations=1)

cv2.imshow("Image_normal",img)
cv2.imshow("Gray scale",imgray)
cv2.imshow("IMage BLur",imgblur)

cv2.imshow("Edge detector",imgCanny)

cv2.imshow("IDilation",imgdilation)

cv2.imshow("erode",imgerode)
cv2.waitKey(0)