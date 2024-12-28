import cv2
import numpy as np

img = cv2.imread("resources/img01.jpg")

# pts1=np.float32([[10,10],[15,25],[10,26],[25,24]])
# print(pts1)
#
# cv2.circle(img ,(pts1[0][0],pts1[0][1]),5,(0,255,0),cv2.FILLED)

width,height = 250,350
pts1 = np.float32([[111,219],[287,188],[154,282], [352 , 240]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))
for x in range(4):
    cv2.circle(img,(pts1[x][0],pts1[x][1]),15,(0,255,0),cv2.FILLED)

cv2.imshow("images",img)
cv2.imshow("image",imgOutput)
cv2.waitKey(1)