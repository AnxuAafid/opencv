import cv2 as cv
import sys
"""
_______________________________
 01. Understand the working of imread , waitkey and imwrite
_______________________________

"""
img = cv.imread("resources/im2.jpg")

if img is None:
    sys.exit("Could not read the image.")

cv.imshow("Display window", img)
k = cv.waitKey(0)
# if user presses the key s it will save the image otherwise will quit
if k == ord("s"):
    cv.imwrite("starry_night.png", img)