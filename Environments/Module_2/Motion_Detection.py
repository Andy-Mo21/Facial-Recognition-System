import cv2
import  numpy as np

webcam = cv2.VideoCapture('Footage/Mall_footage.mp4')

rect, frame1 = webcam.read()
rect, frame2 = webcam.read()
while True:

    if frame1 is None or frame2 is None:
       break

    abs_diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(abs_diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    __, thresh = cv2.threshold(blur, 127, 250, cv2.THRESH_BINARY)
    kernel = np.ones((2, 3), dtype= np.int8)
    dilate = cv2.dilate(thresh, kernel, iterations=4)

    font = cv2.FONT_HERSHEY_SIMPLEX

    contours, __ = cv2.findContours(dilate, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    for contours in contours:
        (x, y, w, h) = cv2.boundingRect(contours)

        if cv2.contourArea(contours) < 700:
            continue
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 1)
        cv2.putText(frame1, 'Status: {}'.format('Movement'), (20, 30), font, 1, (0, 0, 255), 2)



    cv2.imshow('Frame', frame1)

    frame1 = frame1
    rect, frame1 = webcam.read()

    if cv2.waitKey(1) & 0XFF == 32:
        break

webcam.release()
cv2.destroyAllWindows()