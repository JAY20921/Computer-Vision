import cv2
import mediapipe as mp
import pyautogui
import time

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
drawing_utils = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

last_action_time = time.time()
action_delay = 0.245
middle_zone_threshold = 0.05

def get_distance(a, b):
    return ((a.x - b.x) ** 2 + (a.y - b.y) ** 2) ** 0.5

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            drawing_utils.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            wrist = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            middle_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
            ring_tip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
            pinky_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]

            wrist_x = wrist.x
            wrist_y = wrist.y

            movement_threshold = 0.02

            if 0.45 < wrist_x < 0.55 and 0.45 < wrist_y < 0.55:
                action_delay = 1.0
                print("Hand in middle, no action.")
            else:
                action_delay = 0.5

            if time.time() - last_action_time > action_delay:
                if wrist_x < 0.4:
                    pyautogui.press('left')
                    print("Move Left")
                    last_action_time = time.time()

                elif wrist_x > 0.6:
                    pyautogui.press('right')
                    print("Move Right")
                    last_action_time = time.time()

                if wrist_y < 0.4:
                    pyautogui.press('up')
                    print("Move Up")
                    last_action_time = time.time()

                elif wrist_y > 0.6:
                    pyautogui.press('down')
                    print("Move Down")
                    last_action_time = time.time()

    cv2.imshow("Hand Gesture to Keyboard", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
