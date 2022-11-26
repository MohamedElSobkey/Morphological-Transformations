import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('smarties.png', 0)
_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)



kernal = np.ones((5,5), np.uint8)
dilation = cv2.dilate(mask, kernal, iterations=2)
erosion = cv2.erode(mask, kernal , iterations = 1)
#performing erosion then performing dilation
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN ,kernal, iterations = 1)
#performing dilation then performing erosion 
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE ,kernal, iterations = 1)

cv2.imshow('gray image', img)
cv2.imshow('mask', mask)
cv2.imshow('after dilation', dilation)
cv2.imshow('after erosion', erosion)
cv2.imshow('after opening', opening)
cv2.imshow('after closing', closing)



cv2.waitKey(0)
cv2.destroyAllWondows()
