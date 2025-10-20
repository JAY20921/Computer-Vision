import cv2 as cv
import mediapipe as mp
import numpy as np
import time

cap = cv.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

img = np.zeros((600, 800, 3), dtype=np.uint8)

rows, cols = 4, 5 
rect_width, rect_height = 55, 55  
x_start, y_start = 10, 10  
x_spacing, y_spacing = 5, 5 


buttons = [
    ['7', '8', '9', '/', 'Reset'],  
    ['4', '5', '6', '*', ''],
    ['1', '2', '3', '-', ''],
    ['0', '.', '=', '+', '']
]


button_color = (200, 200, 200)
active_color = (0, 255, 0)  


input_text = ""
output_text = ""


last_tap_time = time.time()
tap_threshold = 2  


def draw_calculator(img, active_button=None):
    for i in range(rows):
        for j in range(cols):
            x1 = x_start + j * (rect_width + x_spacing)
            y1 = y_start + i * (rect_height + y_spacing)
            x2 = x1 + rect_width
            y2 = y1 + rect_height

          
            button_color_to_use = active_color if (i, j) == active_button else button_color

            cv.rectangle(img, (x1, y1), (x2, y2), button_color_to_use, -1)

            if buttons[i][j]:  
                cv.putText(img, buttons[i][j], (x1 + 20, y1 + 40), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv.LINE_AA)

def is_finger_on_button(cx, cy):
    for i in range(rows):
        for j in range(cols):
            x1 = x_start + j * (rect_width + x_spacing)
            y1 = y_start + i * (rect_height + y_spacing)
            x2 = x1 + rect_width
            y2 = y1 + rect_height

            if x1 < cx < x2 and y1 < cy < y2:
                return i, j
    return None, None

def handle_calculator_logic(button):
    global input_text, output_text  
    
    if button == '=':
        try:
            output_text = str(eval(input_text))
        except Exception as e:
            output_text = "Error"
        input_text = output_text
    elif button == '.':
        if '.' not in input_text:
            input_text += '.'
    elif button == 'Reset':
       
        input_text = ""
        output_text = ""
    else:
        input_text += button

while True:
    success, img = cap.read()
    imgRGB = cv.cvtColor(img, cv.COLOR_RGB2BGR)
    results = hands.process(imgRGB)

    active_button = None  

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)

                
                draw_calculator(img, active_button) 
                cv.circle(img, (cx, cy), 5, (255, 0, 0), cv.FILLED)

                if id == 8: 
                    row, col = is_finger_on_button(cx, cy)
                    if row is not None and col is not None:
                        button = buttons[row][col]
                        print(f"Finger on: {button}")

                        
                        current_time = time.time()
                        if current_time - last_tap_time > tap_threshold:
                            
                            handle_calculator_logic(button)
                            last_tap_time = current_time  
                            active_button = (row, col)  
                    
                    cv.putText(img, f"Input: {input_text}", (50, 350), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv.LINE_AA)
                    cv.putText(img, f"Output: {output_text}", (50, 450), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv.LINE_AA)

    
    cv.imshow("Calculator", img)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
