# import cv2
# import numpy as np
# import time


# prototxt_path = r"C:\Users\acer\Desktop\OPENCV CAM\MobileNetSSD_deploy.prototxt.txt"
# model_path = r"C:\Users\acer\Desktop\OPENCV CAM\MobileNetSSD_deploy.caffemodel"


# net = cv2.dnn.readNetFromCaffe(prototxt_path, model_path)

# net.setPreferableBackend(cv2.dnn.DNN_BACKEND_DEFAULT)
# net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)


# CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
#            "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
#            "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
#            "sofa", "train", "tvmonitor"]


# cap = cv2.VideoCapture(0)

# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# if not cap.isOpened():
#     print("Error: Cannot open camera")
#     exit()

# while True:
#     start_time = time.time()
#     ret, frame = cap.read()
#     if not ret:
#         break

#     (h, w) = frame.shape[:2]
    
   
#     blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 0.007843,
#                                  (300, 300), 127.5)
#     net.setInput(blob)
#     detections = net.forward()
    
    
#     for i in range(detections.shape[2]):
#         confidence = detections[0, 0, i, 2]
       
#         if confidence > 0.5:
#             idx = int(detections[0, 0, i, 1])
#             # Only process detections labeled as "person"
#             if CLASSES[idx] == "person":
#                 box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
#                 (startX, startY, endX, endY) = box.astype("int")
#                 cv2.rectangle(frame, (startX, startY), (endX, endY),
#                               (0, 255, 0), 2)
#                 label = f"Person: {confidence * 100:.1f}%"
#                 y = startY - 10 if startY - 10 > 10 else startY + 10
#                 cv2.putText(frame, label, (startX, y),
#                             cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
#                 centerX = (startX+endX)//2
#                 centerY = (startY+endY)//2
#                 cv2.circle(frame, (centerX, centerY), 5, (0, 255,255),-1)
#                 label = f"Person: {confidence * 100:.1f}% Pos: ({centerX}, {centerY})"
#                 y = startY - 10 if startY - 10 > 10 else startY + 10
#                 cv2.putText(frame, label, (startX, y),
#                             cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    
   
#     fps = 1 / (time.time() - start_time)
#     cv2.putText(frame, f"FPS: {fps:.2f}", (10, 30),
#                 cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    
#     cv2.imshow("Human Detection ", frame)
    
   
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()


import cv2
import numpy as np
import time


camera_matrix = np.array([[800,   0, 320],
                          [  0, 800, 240],
                          [  0,   0,   1]], dtype="float32")
dist_coeffs = np.array([0.1, -0.25, 0, 0, 0], dtype="float32")  


prototxt_path = r"C:\Users\acer\Desktop\OPENCV CAM\MobileNetSSD_deploy.prototxt.txt"
model_path = r"C:\Users\acer\Desktop\OPENCV CAM\MobileNetSSD_deploy.caffemodel"
net = cv2.dnn.readNetFromCaffe(prototxt_path, model_path)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_DEFAULT)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
           "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
           "sofa", "train", "tvmonitor"]


KNOWN_HEIGHT = 1.7

focal_length = camera_matrix[0, 0]


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

if not cap.isOpened():
    print("Error: Cannot open camera")
    exit()

while True:
    start_time = time.time()
    ret, frame = cap.read()
    if not ret:
        break

    
    undistorted_frame = cv2.undistort(frame, camera_matrix, dist_coeffs)
    (h, w) = undistorted_frame.shape[:2]

   
    blob = cv2.dnn.blobFromImage(cv2.resize(undistorted_frame, (300, 300)), 0.007843,
                                 (300, 300), 127.5)
    net.setInput(blob)
    detections = net.forward()


    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.5:
            idx = int(detections[0, 0, i, 1])
            if CLASSES[idx] == "person":
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")
                cv2.rectangle(undistorted_frame, (startX, startY), (endX, endY), (0, 255, 0), 2)
                
          
                pixel_height = endY - startY
                if pixel_height > 0:
                
                    distance = (KNOWN_HEIGHT * focal_length) / pixel_height
                else:
                    distance = 0

                label = f"Person: {confidence*100:.1f}%  {distance:.2f}m"
                y = startY - 10 if startY - 10 > 10 else startY + 10
                cv2.putText(undistorted_frame, label, (startX, y),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                
           
                centerX = (startX + endX) // 2
                centerY = (startY + endY) // 2
                cv2.circle(undistorted_frame, (centerX, centerY), 5, (0, 255, 255), -1)

    
    fps = 1 / (time.time() - start_time)
    cv2.putText(undistorted_frame, f"FPS: {fps:.2f}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

  
    cv2.imshow("Human Detection with Distance Estimation", undistorted_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
