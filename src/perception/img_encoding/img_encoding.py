#!/usr/bin/env python
import cv2
import numpy as np

color_img = cv2.imread("/home/krzysztof/catkin_ws/src/hello_world/src/perception/img_encoding/knr.jpg", cv2.IMREAD_COLOR)

cv2.imshow("Original Image", color_img)
cv2.moveWindow("Original Image", 0, 0)
print("Ksztaly obrazu RGB {}".format(color_img.shape))

height, width, channels = color_img.shape

print("Split img into RGB channels: ")
blue, green, red = cv2.split(color_img)

cv2.imshow("Blue channel", blue)
cv2.moveWindow("Blue channel", 0,height)

cv2.imshow("Green channel", green)
cv2.moveWindow("Green channel", width, 0)

cv2.imshow("Red channel", red)
cv2.moveWindow("Red channel", width,height)

#konwersja obrazu do HSV
hsv = cv2.cvtColor(color_img,cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)
hsv_img = np.concatenate((h, s, v), axis = 1)
cv2.imshow("HSV Image", hsv_img)
cv2.moveWindow("HSV Image",2*width,0)

#konwersja obrazu do HSV
gray_img = cv2.cvtColor(color_img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image", gray_img)
cv2.moveWindow("Gray Image",2*width,height)



cv2.waitKey(0)
cv2.destroyAllWindows()