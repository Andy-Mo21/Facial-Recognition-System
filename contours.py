import cv2 

img = cv2.imread('Images/cats.jpg')

cv2.imshow('Cats', img)

gray = cv2.cvtColor(img,  cv2.COLOR_RGB2GRAY)
cv2.imshow('Gray', gray)

blur = cv2.GaussianBlur(gray,  (5, 5), cv2.BORDER_DEFAULT)
#cv2.imshow('Blur', blur)

canny = cv2.Canny(blur, 127, 200)
#cv2.imshow('Canny', canny)

rect, thresh = cv2.threshold(gray, 127, 250, cv2.THRESH_BINARY)
print(f'{len(thresh)} countor(s) found')
cv2.imshow('Thresh', thresh)

contours, hierarchies = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found')

cv2.waitKey(0)