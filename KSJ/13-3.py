import cv2
global img1, img2

def on_change_weight(x):
    weight = x/100;
    img_merged = cv2.addWeighted(img1,1-weight,img2,weight,0)
    cv2.imshow('Display',img_merged)

cv2.namedWindow('Display')
cv2.createTrackbar('weight','Display',0,100,on_change_weight)

img1 = cv2.imread('C:\Temp\green_back.png')
img2 = cv2.imread('C:\Temp\iceberg.png')
img1 = cv2.resize(img1,(300,400))
img2 = cv2.resize(img2,(300,400))

