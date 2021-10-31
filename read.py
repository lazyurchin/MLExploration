import cv2 as cv

img = cv.imread('resources/photos/cat.jpg')
print(img)

cv.imshow('Cat', img)

# Wait indefinitely
cv.waitKey(0)

# VideoCapture(0) --> webcam
# VideoCapture(1) --> next camera source
capture = cv.VideoCapture('resources/videos/dog.mp4')

# while True:
#     isTrue, frame = capture.read()
#     cv.imshow('Video', frame)
#
#     # exit on pressing d key
#     if cv.waitKey(20) & 0xFF == ord('d'):
#         break

capture.release()
cv.destroyAllWindows()
