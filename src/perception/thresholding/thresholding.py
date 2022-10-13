#!/usr/bin/env python

import cv2
import numpy as np


def read_image(image_name, as_gray):
    if as_gray:
        image = cv2.imread(image_name, cv2.IMREAD_GRAYSCALE)
    else:
        image = cv2.imread(image_name, cv2.IMREAD_COLOR)
    return image

def basic_thresholding(gray_iamge, thresholding_value):
    ret, thresh_basic = cv2.threshold(gray_iamge, thresholding_value, 255, cv2.THRESH_BINARY)
    cv2.imshow('Basic Binary Image', thresh_basic)
    cv2.moveWindow('Basic Binary Image', 0, 00)

def adaptive_thresholding(gray_image, thresholding_value):
    adaptive_thresholded_image = cv2.adaptiveThreshold(gray_image, 
                                                        255, 
                                                        cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                                        cv2.THRESH_BINARY_INV, 
                                                        thresholding_value, 
                                                        2)
    x= adaptive_thresholded_image.shape[0]
    cv2.imshow('Adaptive Binary Image', adaptive_thresholded_image)
    cv2.moveWindow('Adaptive Binary Image', 0, x)
def main():
    image_name = '/home/krzysztof/catkin_ws/src/hello_world/src/perception/thresholding/knr.jpg'
    as_gray = True
    gray_image = read_image(image_name, as_gray)
    thresholding_value = 155
    basic_thresholding(gray_image, thresholding_value)
    adaptive_thresholding(gray_image, thresholding_value)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
    