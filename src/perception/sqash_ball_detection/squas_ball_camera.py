#!/usr/bin/env python

import numpy as np
import cv2

def read_img(image_name, show, as_gray):
    
    if as_gray:
        image = cv2.imread(image_name, cv2.IMREAD_GRAYSCALE)
    else:
        image = cv2.imread(image_name, cv2.IMREAD_COLOR)
    if show:
        cv2.imshow('READ_IMAGE',image)
    else:
        pass
    return image
def conver_RGB_2_HSV(image_rgb, show):
    image_hsv = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2HSV)
    if show:
        cv2.imshow('HSV IMAGE', image_hsv)
    else:
        pass
    return image_hsv

# def color_filtering(image_hsv, lower_color, upper_color):
#     mask = cv2.inRange(image_hsv, lower_color, upper_color)
#     cv2.imshow('MASK IMAGE', mask)
#     return mask

def adaptive_thresholding(gray_image, thresholding_value):
    adaptive_thresholded_image = cv2.adaptiveThreshold(gray_image, 
                                                        255, 
                                                        cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                                        cv2.THRESH_BINARY_INV, 
                                                        thresholding_value, 
                                                        2)
    cv2.imshow('Binary', adaptive_thresholded_image)                                                   
    return adaptive_thresholded_image

def basic_thresholding(gray_iamge, thresholding_value):
    ret, thresh_basic = cv2.threshold(gray_iamge, thresholding_value, 255, cv2.THRESH_BINARY_INV)
    cv2.imshow('Basic Binary Image', thresh_basic)
    return thresh_basic

def contours(mask):
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contours

def process_contours(contours, image_rgb):
    
    for c in contours:
        area = cv2.contourArea(c)
        #((x, y), radius) = cv2.minEnclosingCircle(c)
        if area > 200 and area < 4000 :
            cv2.drawContours(image_rgb, [c], -1, (255, 0, 255), 2)
            cx, cy = get_contour_center(c)
            cv2.circle(image_rgb, (cx, cy), 3, (255, 100, 255), 1)
    cv2.imshow('Processed contours',image_rgb)  
def get_contour_center(contour):
    M = cv2.moments(contour)
    cx=-1
    cy=-1
    if (M['m00']!=0):
        cx= int(M['m10']/M['m00'])
        cy= int(M['m01']/M['m00'])
    return cx, cy

def main():
    #image_name = '/home/krzysztof/catkin_ws/src/hello_world/src/perception/sqash_ball_detection/squash_ball_2.jpg'
    #lower_color = (0, 0, 0)
    #upper_color = ( 35, 0, 25)
    
    captured_video = cv2.VideoCapture(0)
    if not captured_video.isOpened():
        print("Cannot open camera")
        exit()
    while True:
        # Capture frame-by-frame
        ret, frame = captured_video.read()
        # if frame is read correctly ret is True
        image_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        mask = basic_thresholding(image_gray, 83)
        contour = contours(mask)        
        process_contours(contour, image_gray)
        if cv2.waitKey(25) == ord('q'):
            break
    # When everything done, release the capture
    captured_video.release()
    cv2.destroyAllWindows() 

if __name__ =='__main__':
    main()