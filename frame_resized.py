import cv2 


def webcam_release(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimension = (width, height)


    return cv2.resize(frame, dimension, interpolation=cv2.INTER_AREA)

WebCam = cv2.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = WebCam.read()

    resized = webcam_release(frame)

    cv2.imshow('Frame', frame)
    cv2.imshow('Resized Frame', resized )

    if cv2.waitKey(20) & 0XFF == ord('d'):
        break

WebCam.release()
cv2.destroyAllWindows()

