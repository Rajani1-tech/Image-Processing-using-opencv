# in this project threshold value is taken from the user as a input.
import numpy as np
import cv2
img=cv2.imread('photo/tu.png',0)
w,h= img.shape
th= int(input('Enter the threshold value'))
print(th)
th_img=np.array(img)
for x in range(w):
    for y in range(h):
        if img[x,y]<=th:
            th_img[x,y]=0
        else:
            th_img[x,y]=255
cv2.imshow('originalImage', img)
cv2.imshow('Threshold', th_img)
cv2.waitKey(0)
