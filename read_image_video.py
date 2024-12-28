"""#     To READ ANY IMAGE
import cv2
img= cv2.imread("resources/img01.jpg",)
cv2.imshow("Image",img)
cv2.waitKey(10000) # lets to wait the screen , for infinity wait pass 0 as argument

"""

#to read a video

import cv2
framewidth = 620
frameheight = 100

cap = cv2.VideoCapture("resources/ved.mp4")


"""
# for using the default camera use here 
cap=cv2.VideoCapture(0)
cap.set(3,framewidth)
cap.set(4,framewidth)"""

while True:
    sucess , img =cap.read()
    img= cv2.resize(img,(framewidth,frameheight))
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break