import cv2 as cv
import numpy as np

# HSV ranges
lower_red1 = np.array([0, 100, 100])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([160, 100, 100])
upper_red2 = np.array([179, 255, 255])

# Yellow / Light yellow apples
lower_yellow = np.array([20, 50, 150])
upper_yellow = np.array([35, 200, 255])

kernel = np.ones((3,3), np.uint8)

video = cv.VideoCapture(0)

while True:
    success, frame = video.read()
    if not success:
        break

    # Resize for speed but keep enough detail
    frame = cv.resize(frame, (640, 480))

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # Masks for colors
    mask_red1 = cv.inRange(hsv, lower_red1, upper_red1)
    mask_red2 = cv.inRange(hsv, lower_red2, upper_red2)
    mask_yellow = cv.inRange(hsv, lower_yellow, upper_yellow)

    # Combine masks
    mask = cv.bitwise_or(mask_red1, mask_red2)
    mask = cv.bitwise_or(mask, mask_yellow)

    # Morphology to remove noise
    mask = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)
    mask = cv.morphologyEx(mask, cv.MORPH_DILATE, kernel)

    # Find contours
    contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        if cv.contourArea(cnt) > 500:
            x, y, w, h = cv.boundingRect(cnt)
            cv.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
            # Centroid
            M = cv.moments(cnt)
            if M["m00"] != 0:
                cx = int(M["m10"]/M["m00"])
                cy = int(M["m01"]/M["m00"])
                cv.circle(frame, (cx, cy), 4, (255, 0, 0), -1)

    cv.imshow("Mask", mask)
    cv.imshow("Apple Detection", frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv.destroyAllWindows()
