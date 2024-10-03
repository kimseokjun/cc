import cv2

img =cv2.imread("C:\Temp\mandrill.png",1)
cv2.rectangle(img, (10,200), (200,20),(0,0,0),5)
cv2.line(img,(10,20), (200,200), (0,0,255),5) #이미지, 시작지점, 끝지점, 색상, 굵기

cv2.arrowedLine(img, (10,200), (200,20), (0,0,255),5)


cv2.putText(img, "hello",(70,70),fontFace=2,fontScale=1,color=(0,0,0))
cv2.imshow('lined' ,img)
