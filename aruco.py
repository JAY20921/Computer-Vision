import cv2
import numpy as np

def perform_task(marker_id):
    """
    Perform a task based on the detected marker ID.
    """
    if marker_id == 1:
        print("Marker 1 detected! Performing Task 1...")
    elif marker_id == 2:
        print("Marker 2 detected! Performing Task 2...")
    else:
        print(f"Marker {marker_id} detected, but no task defined for this marker.")

def detect_aruco_markers():
    cap = cv2.VideoCapture(0)

    aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
    
    parameters = cv2.aruco.DetectorParameters()

    while True:
        
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break


        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


        corners, ids, rejected_img_points = cv2.aruco.detectMarkers(gray, aruco_dict, parameters=parameters)

       
        if ids is not None:

            cv2.aruco.drawDetectedMarkers(frame, corners, ids)
            for marker_id in ids.flatten():
                perform_task(marker_id)  

     
        cv2.imshow("ArUco Marker Detection", frame)

        if cv2.waitKey(1) & 0xFF == 27:  
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detect_aruco_markers()
