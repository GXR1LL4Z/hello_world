#!/usr/bin/env python

import numpy as np
import cv2

def rgb_image(image, show):
    #pobranie obrazu w kodowaniu RGB
    image_rgb = cv2.imread(image)
    image_rgb = cv2.resize(image_rgb, (0,0), fx = 0.7, fy = 0.7)
    if show:
        cv2.imshow('RGB IMAGE', image_rgb)
    else:
        pass
    return image_rgb

def convert_rgb_to_gray(image_rgb, show):
    #zmiana kodowania obrazu z RGB na GRAY_SCALE
    image_gray_scale = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2GRAY)
    if show:
        cv2.imshow('GRAY SCALE IMAGE', image_gray_scale)
    else:
        pass
    return image_gray_scale

def convert_gray_to_binary(image_gray_scale, adaptive, show):
    #zmiana kodowania (poprzez thresholding) z gray scale na binary
    if adaptive:
        image_binary = cv2.adaptiveThreshold(image_gray_scale,                      #obraz
                                            255,                                    #max_value
                                            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,         #adaptive method
                                            cv2.THRESH_BINARY_INV,                  #threshold type
                                            115,                                    #blok size                         
                                            2)                                      #const
    else:
        _, image_binary = cv2.threshold(image_gray_scale,127,255,cv2.THRESH_BINARY_INV)
    if show:
        cv2.imshow('BINARY IMAGE', image_binary)
    else:
        pass
    return image_binary

def getCountours(image_binary):
    #pobranie konturw z obarazu binary i zwrocenie takiego obiektu
    contures, hierarchy = cv2.findContours(image_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contures

def drawCountours(image_to_draw, contours, name_of_image):
    #narysowanie konturow na pierwotnym obrazie RGB
    index = -1
    thickness = 2
    color = (255,0,255)
    cv2.drawContours(image_to_draw, contours, index, color, thickness)
    cv2.imshow(name_of_image, image_to_draw)
    

def main():
    #definicja sciezki do obrazka
    image = '/home/krzysztof/catkin_ws/src/hello_world/src/perception/edge_detection/czerwona_pilka.jpg' 
    show = True
    adaptive = True
    image_rgb = rgb_image(image, show)
    image_gray_scale = convert_rgb_to_gray(image_rgb, show)
    image_binary = convert_gray_to_binary(image_gray_scale, adaptive, show)
    contours = getCountours(image_binary)
    drawCountours(image_rgb, contours, 'CONTURES ON RGB')

    #zaczekaj na przycisk 0 i zniszc wszytskie okna
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()