import numpy as np
import cv2

org = cv2.imread('C:\Temp\mandrill.png')

kernel1 = np.ones((3,3),np.float32)/9
kernel2 = np.ones((9,9),np.float32)/81

averaged33 = cv2.GaussianBlur(org,(3,3),1)
averaged99 = cv2.GaussianBlur(org,(9,9),1)

cv2.imshow('original',org)
cv2.imshow('Gaussian 33',averaged33)
cv2.imshow('Gaussian 99',averaged99)
