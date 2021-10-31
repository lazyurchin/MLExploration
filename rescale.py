import cv2 as cv

def rescaleFrame(frame, scale=0.25):
    # frame.shape[1] gives the width of the frame
    width = int(frame.shape[1] * scale)
    # frame.shape[0] gives the height of the frame
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


capture = cv.VideoCapture('resources/videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)
    cv.imshow('Video', frame_resized)

    # exit on pressing d key
    if cv.waitKey(20) & 0xFF == ord('d'):
        breakcapture = cv.VideoCapture('resources/videos/dog.mp4')

capture.release()
cv.destroyAllWindows()


