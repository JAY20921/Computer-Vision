import cv2 as cv
import numpy as np

cam = cv.VideoCapture(0)
while True:
    frame, ret = cam.read()
    if not ret:
        break

cv.waitKey()
