import cv2

## Read an image
# img = cv2.imread('resources/car1.jpeg')
# print(img)
# print(img.shape)
# cv2.imshow('image', img)


## Read a video
# cap = cv2.VideoCapture('resources/elon.mp4')
# while True:
#     success, img = cap.read()
#     if not success:
#         break
#     print (img.shape)
#     cv2.imshow('video', img)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break


## Read from webcam
cap = cv2.VideoCapture(0)

cap.set(3, 640) # Width
cap.set(4, 480) # Height
cap.set(10, 100) # Brightness

while True:
    success, img = cap.read()
    print (img.shape)
    cv2.imshow('video', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break