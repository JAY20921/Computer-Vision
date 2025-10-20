import cv2 as cv
from cvzone.HandTrackingModule import HandDetector

cap = cv.VideoCapture(0)
detector = HandDetector(maxHands=1, detectionCon=0.7)

while True:
    success, img = cap.read()
    if not success:
        print("Failed to capture image from webcam.")
        break

    hands, img = detector.findHands(img)

    if hands:
        lmList = hands[0]['lmList']  
        bbox = hands[0]['bbox']      

        
        print("Landmarks:", lmList)
        print("Bounding Box:", bbox)

    
    cv.imshow("Image", img)

    
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
