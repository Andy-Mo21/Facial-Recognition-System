import cv2 

webcam = cv2.VideoCapture(0)

haar_cascade = cv2.CascadeClassifier('haar_cascade.xml')

while True:

    rect, frame = webcam.read()

    if not rect:
        break


    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_detect = haar_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=6)

    for (x, y, w, h) in face_detect:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        print(f'Number(s) of faces found = {len(face_detect)}' )

    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) & 0XFF == 32:
        break

webcam.release()

cv2.destroyAllWindows()