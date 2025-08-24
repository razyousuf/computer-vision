import cv2

## Read an image
# img = cv2.imread('resources/car1.jpeg')
# print(img)
# print(img.shape)
# cv2.imshow('image', img)


## Read a video
cap = cv2.VideoCapture('resources/elon.mp4')
while True:
    success, img = cap.read()
    if not success:
        break
    cv2.imshow('video', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


## Read from webcam
