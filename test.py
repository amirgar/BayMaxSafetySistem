import time
import cv2


cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    cv2.imshow('video feed', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break