import cv2
import requests
import time

# Function to upload file to a server
def upload_file(file_path, url):
    with open(file_path, 'rb') as file:
        files = {'file': file}
        response = requests.post(url, files=files)
        return response.text

# Initialize video capture
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

# Record for 10 seconds
start_time = time.time()
while(int(time.time() - start_time) < 10):
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture image.")
        break
    out.write(frame)

# Release everything when the job is finished
cap.release()
out.release()
cv2.destroyAllWindows()

# Upload the video to a server
upload_url = 'http://localhost:8000'  # Replace with your server URL
response = upload_file('output.avi', upload_url)
print("Upload Response:", response)