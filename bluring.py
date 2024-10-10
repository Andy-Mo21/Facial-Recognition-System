import cv2 

img = cv2.imread('Images/cats.jpg')
cv2.imshow('Cats Original', img )

# Average Bluring
blur = cv2.blur(img, (3, 3))
cv2.imshow('Blur', blur)

# Gaussina blur 
Gauss = cv2.GaussianBlur(img, (3, 3), 0)
cv2.imshow('Gaus', Gauss)

# Median Blur
Median  = cv2.medianBlur(img, 3)
cv2.imshow('Median', Median)


#Bilateral Bluring
bilateral = cv2.bilateralFilter(img, 3, 10, 15)
cv2.imshow('Bilateral Blur', bilateral)

cv2.imread('Original', img)

cv2.waitKey(0)