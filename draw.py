import cv2 

import numpy as np


blank = np.zeros((500, 500, 3), dtype= 'uint8')
cv2.imshow('Blank', blank)

# Drawing colour on blank surfaces

blank[200:300, 300:400] = (0, 0, 150)
cv2.imshow('Green', blank)

# Drawnig rectangle
point1 = (0, 0)
point2 = (250, 500)

cv2.rectangle(blank,point1, (blank.shape[0]//2, blank.shape[1]//2), (0, 255, 0), -1)
cv2.imshow('Rectangle', blank)

# Drawing circle 

cv2.circle(blank, (blank.shape[0]//2, blank.shape[1]//2), 50, (0, 0,255), 2, -1)
cv2.imshow('Circle', blank)

#Drwaing a line
cv2.line(blank, (0, 200), (200, 300), (255,255,255), 2)
cv2.imshow('Line', blank )

cv2.putText(blank,'Hello, This is Andy Mo', (0, 250), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 100, 0), 1)
cv2.imshow('Text', blank)



cv2.waitKey(0)
cv2.destroyAllWindows()