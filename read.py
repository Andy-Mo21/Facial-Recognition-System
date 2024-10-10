import cv2

#img = cv2.imread('Images/cat_large.jpg')

#cv2.imshow('Cat', img)


webcam = cv2.VideoCapture('Videos/dog.mp4')

while True:
    __, frame = webcam.read()

    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) & 0XFF== ord('q'):
        break


webcam.release()
cv2.destroyAllWindows()