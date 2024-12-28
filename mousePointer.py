import cv2
import numpy as np


circles = np.zeros((4,2),int)
print(circles)
counter = 0

def mousePoints(event,x,y,flags,params):
    global counter,circles
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,y)
        circles[counter] = x,y
        counter += 1
        print(circles)

img = cv2.imread("resources/im4.jpeg")

while True:
    if counter==4:
        width, height = 250, 350
        pts1 = np.float32([circles[0], circles[1], circles[2], circles[3]])
        pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        imgOutput = cv2.warpPerspective(img, matrix, (width,height))
        cv2.imshow("output Image", imgOutput)

    for x in range(4):
        cv2.circle(img, (circles[x][0], circles[x][1]), 5, (0, 255, 0), cv2.FILLED)
    cv2.imshow("Original Image", img)
    cv2.setMouseCallback("Original Image",mousePoints)
    cv2.waitKey(1)