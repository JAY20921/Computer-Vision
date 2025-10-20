import cv2
import numpy as np
import requests
import time

# ESP32 server URL
ESP32_URL = "http://192.168.47.117"  # Replace with your ESP32 IP address

def send_command_to_esp32(fingers):
    """Send the number of fingers detected to ESP32."""
    try:
        response = requests.get(f"{ESP32_URL}/control?lights={fingers}")
        print(f"ESP32 Response: {response.text}")
    except Exception as e:
        print(f"Failed to send data to ESP32: {e}")

def count_fingers(frame):
    """Count the number of fingers in the frame."""
    # Convert to gray and blur
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (35, 35), 0)

    # Threshold
    _, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if not contours:
        return 0

    # Filter small contours (noise)
    max_contour = max(contours, key=cv2.contourArea)
    if cv2.contourArea(max_contour) < 5000:  # Minimum area to consider as a hand
        return 0

    # Create convex hull
    hull = cv2.convexHull(max_contour)

    # Find convexity defects
    hull_indices = cv2.convexHull(max_contour, returnPoints=False)
    defects = cv2.convexityDefects(max_contour, hull_indices)

    if defects is None:
        return 0
    
    # Count defects (fingers)
    fingers = -1
    for i in range(defects.shape[0]):
        s, e, f, d = defects[i, 0]
        start = tuple(max_contour[s][0])
        end = tuple(max_contour[e][0])
        far = tuple(max_contour[f][0])

        # Apply angle cosine rule to count fingers
        a = np.linalg.norm(np.array(start) - np.array(far))
        b = np.linalg.norm(np.array(end) - np.array(far))
        c = np.linalg.norm(np.array(start) - np.array(end))
        angle = np.arccos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b))

        # Ignore angles greater than 90 degrees and points too close
        if angle <= np.pi / 2 and d > 10000:
            fingers += 1

    return fingers + 1

def main():
    # Start video capture
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    prev_time = time.time()
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Flip frame horizontally for a natural interaction
        frame = cv2.flip(frame, 1)

        # Count fingers
        fingers = count_fingers(frame)

        # Display the result on the screen
        cv2.putText(frame, f"Fingers: {fingers}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("Finger Detection", frame)

        # Send command to ESP32
        send_command_to_esp32(fingers)

        # Calculate FPS
        curr_time = time.time()
        fps = 1 / (curr_time - prev_time)
        prev_time = curr_time
        print(f"FPS: {fps:.2f}", end='\r')

        # Break on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
