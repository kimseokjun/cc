import cv2

original_image = cv2.imread('C:\Temp/salt_pepper.png',0)
result_image1 = cv2.medianBlur(original_image,9)
result_image2 = cv2.GaussianBlur(original_image,(9,9),1)
result_image3 = cv2.bilateralFilter(original_image,9,50,50)

cv2.imshow('original',original_image)
cv2.imshow('medianBlur',result_image1)
cv2.imshow('GaussianBlur',result_image2)
cv2.imshow('bilateralFilter',result_image3)
