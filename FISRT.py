import cv2 as cv
import numpy as np
import os

# blank = np.zeros((500,500,3), dtype='uint8')

# def rescaleFrame(frame,scale = 0.5):
#     width = int(frame.shape[1] * scale)
#     height = int(frame.shape[0] * scale)
#     dimensions = (width, height)
#     return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

# def change_res(width, height):
#    capture.set_res(3, width)
#    capture.set_res(6, height)
# capture = cv.VideoCapture(r"C:\Users\acer\Desktop\OPENCV CAM\2023-11-02 17-20-28.mkv")

# while True:
#    isTrue, frame = capture.read()
   
#    frame_resized = rescaleFrame(frame)
#    cv.imshow('Video',frame_resized)
  

#    if cv.waitKey(20) & 0xFF == ord('d'):
#     break


# capture.realease()
# cv.destroyAllWindows()
#paint image in shape
# blank[200:300, 100:340] = 0,255,0
# cv.imshow('Green',blank)

# rect = cv.rectangle(blank,(50,50),(350,400),(0,255,0),thickness=cv.FILLED)
# cv.imshow('Rectangle',blank)


# cv.circle(blank,(250,250),300,(0,230,400),thickness=30)
# cv.imshow('Circle',blank)
# for i in range(101):
#     cv.line(blank,(i*25,i*23),(i*60,i*25),(255,i,0),thickness=5)
#     cv.imshow('Line',blank)

#write text on image
# cv.putText(blank,'Image',(255-60,255),cv.FONT_HERSHEY_SIMPLEX,1.0,(0,255,0),thickness=1)
# cv.imshow('text',blank)
img = cv.imread(r"C:\Users\acer\Pictures\Camera Roll\WIN_20230805_10_06_01_Pro.jpg")
# cv.imshow('Cat',img)

# cv.imshow('Image',img)

#converting image to grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Grayscale',gray)

#blur
# blur = cv.GaussianBlur(img, (33,43),cv.BORDER_DEFAULT)
# cv.imshow('Blur',blur)

#canny edge detector
# canny = cv.Canny(img,125,175)
# cv.imshow('Canny',canny)

#Dialating image
# dialated = cv.dilate(canny, (3,3), iterations=1)
# cv.imshow('Dial',dialated)

#erosion image
# eroded = cv.erode(dialated,(3,3),iterations=1)
# cv.imshow('Erode',eroded)

# #resize
# resized = cv.resize(img,(500,500),interpolation=cv.INTER_LINEAR)
# cv.imshow('Erode',resized)

# #cropping
# cropped = img[500:2000,1000:2000]
# cv.imshow('Cropped',cropped)

# def translation(img,x,y):
#     transMat = np.float32([[1,0,x],[0,1,y]])
#     dimensions = (img.shape[1],img.shape[0])
#     return cv.warpAffine(img,transMat,dimensions)

# translated = translation(img,100,100)
# cv.imshow('Translation',translated)

# rotate = cv.rotate(img,1)
# cv.imshow('rotated',rotate)
# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# canny = cv.Canny(img,125,175)
# blur = cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT)
# ret, thresh = cv.threshold(gray,125,255, cv.THRESH_BINARY)
# contours, heirarchies = cv.findContours(thresh,cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
# cv.imshow('Thresh',thresh)
# print(f'{len(contours)} contours(s) found!')

# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
 # cv.imshow('Hsv',hsv)
# cv.imshow('Gray',gray)

# Apply threshold
# ret, thresh = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
# Find contours
# contours, hierarchy = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

# Print the number of contours found
# print(f"{len(contours)} contours(s) found")

# Optionally draw the contours on the original image
# cv.drawContours(img, contours, -1, (0, 255, 0), 2)

# # Display the result
# cv.imshow('Contours', img)



# blank = np.zeros(resized.shape[:2],dtype='uint8')
# cv.imshow('resized',resized)
# img = resized
# b,g,r = cv.split(img)

# blue = cv.merge([b,blank,blank])
# green = cv.merge([blank,g,blank])
# red = cv.merge([blank,blank,r])

# cv.imshow('blue',blue)
# cv.imshow('green',green)
# cv.imshow('red',red)

# print(img.shape)
# print(b.shape)
# print(r.shape)
# print(g.shape)

# merged = cv.merge([b,g,r])
# cv.imshow('merge',merged)
resized = cv.resize(img,(1200-200,700-100))
# cv.imshow('resized',resized)
# average = cv.blur(resized,(7,7))
# cv.imshow('average',average)

# gBlur = cv.GaussianBlur(resized,(5,5),0)
# cv.imshow('gBlur',gBlur)

# medianBlur = cv.medianBlur(resized,3)
# cv.imshow('median',medianBlur)

# bilateral = cv.bilateralFilter(resized, 5, 15, 15)
# cv.imshow('bilateral',bilateral)



# blank = np.zeros((400,400), dtype='uint8')
# rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
# circle = cv.circle(blank.copy(), (200,200),  200, 255 , -1)

# cv.imshow('circle',circle)
# cv.imshow('rectangle',rectangle)

# #bitwise AND or not xor
# bitwise_and = cv.bitwise_and(rectangle,circle)

# bitwise_xor = cv.bitwise_xor(rectangle,circle)

# cv.imshow('bitwise xor', bitwise_xor)


# blank = np.zeros(resized.shape[:2],dtype = 'uint8')

# mask = cv.circle(blank, (resized.shape[1]//2,resized.shape[0]//2),190,255,-1)
# cv.imshow('mask',mask)

# masked = cv.bitwise_and(resized, resized, mask=mask)
# cv.imshow('masked', masked)
img = resized
# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# #grayscale histogram
# gray_hist = cv.calcHist([gray], [0],None,[256],[0,256])
# plt.figure()
# plt.title('Grayscale histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# # plt.plot(gray_hist)
# # plt.xlim([0,256])
# # plt.show()

# colors = ('b','g','r')
# for i,col in enumerate(colors):
#     hist = cv.calcHist([img],[i], None, [256], [0,256])
#     plt.plot(hist,color=col)
#     plt.xlim([0,256])
#plt.show()

# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('Gray',gray)

# threshold, thresh = cv.threshold(gray, 150 , 255 , cv.THRESH_BINARY)
# cv.imshow('Threshold', thresh)

# threshold, thresh_inv = cv.threshold(gray, 150 , 255 , cv.THRESH_BINARY_INV)



# #adaptive threshold
# adaptive_threshold = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY, 11,3)
# cv.imshow('Adaptive threshold',adaptive_threshold)

#edge detection
#laplacian method
# lap = cv.Laplacian(gray,cv.CV_64F)
# lap = np.uint8(np.absolute(lap))
# cv.imshow('Laplacian',lap)

# #Sobel
# sobel_x = cv.Sobel(gray,cv.CV_64F, 1,0)
# sobel_y = cv.Sobel(gray,cv.CV_64F, 0,1)
# combined = cv.bitwise_or(sobel_x,sobel_y)

# cv.imshow('combined',combined)

# Canny = cv.Canny(gray,150,175)
# cv.imshow('Canny',Canny)






#####face detection#####

# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('Gray',gray)

# haar_cascade = cv.CascadeClassifier(r"C:\Users\acer\Desktop\OPENCV CAM\haar_face.xml")

# faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.35, minNeighbors=3)

# print(f'Number of faces found = {len(faces_rect)}')

# for (x,y,w,h) in faces_rect:
#     cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0),thickness=2)

# cv.imshow('Detected faces', img)





############face recognition ###############


people = ['SRK','Salman','Deepika','John']
DIR = r'C:\Users\acer\Desktop\OPENCV CAM'
haar_cascade = cv.CascadeClassifier(r"C:\Users\acer\Desktop\OPENCV CAM\haar_face.xml")


features = []
labels = []

def create_train():
    for person in people:
        path = os.path.join(DIR,person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path,img)
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)

            face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
            
            for (x,y,w,h) in face_rect:
                face_roi = gray[y:y+h, x:x+w]
                features.append(face_roi)
                labels.append(label)

create_train()
print("Training done")

features = np.array(features,dtype='object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

#train the recognizer on the features list and labels list

face_recognizer.train(features,labels)
face_recognizer.save(r"C:\Users\acer\Desktop\OPENCV CAM\face_trained.yml")
np.save('features.npy',features)
np.save('labels.npy',labels)


cv.waitKey(0)
cv.destroyAllWindows()














 