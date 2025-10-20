import cv2
import face_recognition

# Load the reference image
reference_image = face_recognition.load_image_file("reference.jpg")

# Load the target image
target_image = face_recognition.load_image_file("target.jpg")

# Get the face encodings for both images
reference_encoding = face_recognition.face_encodings(reference_image)[0]
target_encoding = face_recognition.face_encodings(target_image)[0]

# Compare the face encodings
distance = face_recognition.face_distance([reference_encoding], target_encoding)

# Check if the distance is less than a certain threshold (e.g., 0.6)
if distance < 0.6:
    print("Both persons are the same.")
else:
    print("Both persons are not the same.")