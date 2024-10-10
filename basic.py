import cv2

image = cv2.imread('Images/park.jpg')
cv2.imshow('Original', image)

# Converting to gray
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#cv2.imshow('Boston Park', gray )

#Bluring images
blur = cv2.GaussianBlur(image, (7, 7), cv2.BORDER_DEFAULT)
#cv2.imshow('Blur', blur)


# Canny edge detector
canny =cv2.Canny(image, 127, 200) # More noise with the orininal image
#cv2.imshow('Canny More', canny)

# Canny with less noise with the blur image
Canny = cv2.Canny(blur, 172, 200)
#cv2.imshow('Canny Less', Canny)

# image Dilation
dilated = cv2.dilate(Canny, (7, 7), iterations=3)
#cv2.imshow('Dilated', dilated)

eroded =cv2.erode(dilated, (7, 7), iterations= 3)
#cv2.imshow('Eroded', eroded)

# Resized
resized = cv2.resize(image, (500, 500), interpolation=cv2.INTER_CUBIC)
cv2.imshow('Resized', resized)

# Cropping
croped = image[200:300, 300:400]
cv2.imshow('Croped', croped)

cv2.waitKey(0)
cv2.destroyAllWindows()
