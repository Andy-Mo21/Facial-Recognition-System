import cv2 
import numpy as np

img = cv2.imread('Images/cats.jpg')

blank = np.zeros(img.shape[:2], dtype='uint8')

mask = cv2.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, (255, 255, 255), -3)
cv2.imshow('Mask', mask)

masked = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow('Masked', masked)


cv2.waitKey(0)
cv2.destroyAllWindows()