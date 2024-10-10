import cv2

img = cv2.imread('Images/standing.jpg')
cv2.imshow('Lady', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  
cv2.imshow('Gray', gray)


haar_cascade = cv2.CascadeClassifier('haar_cascade.xml')

front_face = haar_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=6)

for (x,y,w,h) in front_face:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), thickness=2)

    print(f'Number of faces found: {len(front_face)} ')
    

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()