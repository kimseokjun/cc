import numpy as np
import cv2

image = cv2.imread('C:\Temp\mandrill.png')
image_hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

red_low = np.array([20,0,0])
red_high = np.array([80,255,255])

my_mask = cv2.inRange(image_hsv,red_low,red_high)
cv2.imshow('original',image)
cv2.imshow('mask',my_mask)

