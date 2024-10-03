import numpy as np
import cv2

image = cv2.imread('C:\Temp\mandrill.png')
image_hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

red_low = np.array([0, 50, 50])
red_high = np.array([30, 255, 255])

my_mask = cv2.inRange(image_hsv,red_low ,red_high)
cv2.imshow('original',image)
cv2.imshow('mask',my_mask)

extracted = cv2.bitwise_and(image,image,mask=my_mask)
cv2.imshow('extracted',extracted)
