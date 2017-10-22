import cv2
import numpy as np

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    cv2.imshow("opencv", frame)

    if cv2.waitKey(10) > 0:
        break


cam.release()
cv2.destroyAllWindows()


