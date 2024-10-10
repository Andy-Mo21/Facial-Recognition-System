import cv2
import numpy as np

blank = np.zeros((500, 500), dtype='uint8')

rectangle = cv2.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
cv2.imshow('Rectangle', rectangle)


circle = cv2.circle(blank.copy(), (200, 200), 200, 255, -1)
cv2.imshow('Circle', circle)

# Bitwise OR
bitwise_or = cv2.bitwise_or(rectangle, circle)
cv2.imshow('Bitwise_OR', bitwise_or)

# Bitwise AND
bitwise_and = cv2.bitwise_and(rectangle, circle)
cv2.imshow('Bitwise and', bitwise_and)

# Bitwise_XOR
bitwise_XOR  = cv2.bitwise_xor(rectangle, circle)
cv2.imshow('Bitwise_XOR', bitwise_XOR)

# Bitwise not
bitwise_RNOT = cv2.bitwise_not(rectangle)
cv2.imshow('Bitwise_RNoT', bitwise_RNOT)

bitwise_CNOT = cv2.bitwise_not(circle)
cv2.imshow('Bitwise CNOT', bitwise_CNOT)
cv2.waitKey(0)