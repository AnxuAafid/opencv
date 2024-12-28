import cv2
import numpy as np

path = "resources/img01.jpg"
img = cv2.imread(path)
print(img.shape)

width, height =400,400
imgresize =cv2.resize(img,(width,height))
print(imgresize.shape)

imgcropped = img[300:541,0:800]

cv2.imshow("img",img)
cv2.imshow("imgresize",imgresize)
cv2.imshow("cropped image",imgcropped)
cv2.waitKey(0)