import cv2 as cv
# All the events related to Mouse Click
events = [i for i in dir(cv) if 'EVENT' in i]
print( events )

import numpy as np
import cv2 as cv


# mouse callback function
def draw_circle(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img, (x, y), 10, (255,185 , 0), -1)


# Create a black image, a window and bind the function to window
img = np.zeros((512, 512, 3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image', draw_circle)

while (1):
    cv.imshow('image', img)
    if cv.waitKey(20) & 0xFF == ord("q"):
        break
cv.destroyAllWindows()