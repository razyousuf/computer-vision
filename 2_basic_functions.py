import cv2

img = cv2.imread('resources/lena.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# blur_img = cv2.GaussianBlur(img, (7,7), 0)

# print("Original Image Shape: ", img.shape)
# print("Gray Image Shape: ", img_gray.shape)
# print("Blur Image Shape: ", blur_img.shape)

# cv2.imshow('Image', img)
# cv2.imshow('Gray Image', img_gray)
# cv2.imshow('Blur Image', blur_img)

# cv2.waitKey(0)

# Edge Detection using Canny
blur_img = cv2.GaussianBlur(img_gray, (7,7), 0)
canny_img = cv2.Canny(blur_img, 100, 120)
print("Blur Image Shape: ", blur_img.shape)
print("Canny Image Shape: ", canny_img.shape)

cv2.imshow('Image', img)
cv2.imshow('Gray Image', img_gray)
cv2.imshow('Blur Image', blur_img)
cv2.imshow('Canny Image', canny_img)

cv2.waitKey(0)