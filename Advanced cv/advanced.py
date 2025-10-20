import cv2
import mediapipe as mp
import time
import math

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0


rect_x, rect_y = 300, 100
rect_width, rect_height = 100, 50

rect1_x, rect1_y = 100, 50
rect2_x, rect2_y = 222, 120



while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            tip_coords = {}
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)

                
                if id in [4, 8, 12, 16, 20]:
                    tip_coords[id] = (cx, cy)
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

            
            if 8 in tip_coords:  
                finger_x, finger_y = tip_coords[8]  

                if rect_x < finger_x < rect_x + rect_width and rect_y < finger_y < rect_y + rect_height:
                    rect_x, rect_y = finger_x - rect_width // 2, finger_y - rect_height // 2

            cv2.rectangle(img, (rect_x, rect_y), (rect_x + rect_width, rect_y + rect_height), (200, 100, 0), -1)


            if 12 in tip_coords:  
                 finger_x, finger_y = tip_coords[12]  
                  
                 if rect1_x < finger_x < rect1_x + rect_width and rect1_y < finger_y < rect1_y + rect_height:
                    rect1_x, rect1_y = finger_x - rect_width // 2, finger_y - rect_height // 2

            cv2.rectangle(img, (rect1_x, rect1_y), (rect1_x + rect_width, rect1_y + rect_height), (300, 300, 300), -1)



            if 20 in tip_coords: 
                 finger_x, finger_y = tip_coords[20]  
                  
                 if rect2_x < finger_x < rect2_x + rect_width and rect2_y < finger_y < rect2_y + rect_height:
                    rect2_x, rect2_y = finger_x - rect_width // 2, finger_y - rect_height // 2

            cv2.rectangle(img, (rect2_x, rect2_y), (rect2_x + rect_width, rect2_y + rect_height), (0, 0, 300), -1)
            cv2.putText(img,"1",(rect2_x + rect_width-70, rect2_y + rect_height-20),1,3,(0, 100, 300),5)

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
    
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)

    cv2.imshow("image", img)
    cv2.waitKey(1)
