import cv2
import numpy as np

img = cv2.imread(r"./YUsufcF.jpg")
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)



def updateImg(args):
    type = cv2.getTrackbarPos('type','why')
    value = cv2.getTrackbarPos('value','why')
    _,new = cv2.threshold(img,value,255,type)
    cv2.imshow("why",new)

cv2.imshow("why",img)
cv2.createTrackbar('type', 'why', 0, 4, updateImg)
cv2.createTrackbar('value', 'why', 0, 255, updateImg)

updateImg(0)

cv2.waitKey(0)