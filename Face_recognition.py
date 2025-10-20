import numpy as np
import cv2 as cv 

haar_cascade = cv.CascadeClassifier(r"C:\Users\acer\Desktop\OPENCV CAM\haar_face.xml")
people = ['SRK','Salman','Deepika','John']
# features = np.load('features.npy',allow_pickle=True)
# labels = np.load('labels.npy',allow_pickle=True)


face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read("face_trained.yml")
img = cv.imread(r"c:\Users\acer\AppData\Local\Temp\salman-khan-photos-images-52397.webp")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Person',gray)

#detect face
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)
for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h,x:x+h]

    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label: {people[label]} with confidence of {confidence}')
    cv.putText(img,str(people[label]),(20,20),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),thickness=2)
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)

cv.imshow('Person',img)
cv.waitKey(0)