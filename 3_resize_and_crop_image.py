import cv2
import numpy as np

img = cv2.imread('resources/lambo.png')
print("Original Image Shape: ", img.shape)
# Resize image
# img_resized = cv2.resize(img, (310, 20))
# print("Resized Image Shape: ", img_resized.shape)
# cv2.imshow('Original Image', img)
# cv2.imshow('Resized Image', img_resized)

# Crop image
img_cropped = img[0:200, 250:400] # y1:y2, x1:x2
print("Cropped Image Shape: ", img_cropped.shape)
cv2.imshow('Original Image', img)
cv2.imshow('Cropped Image', img_cropped)


cv2.waitKey(0)
cv2.destroyAllWindows()