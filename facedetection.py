import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Read the input image
img = cv2.imread('Debjit_Eco.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1 , 4)

for (x, y, w, h) in faces:
	cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 3)

#Dispaly the output

cv2.imshow('Debjit_Eco', img)
cv2.waitKey()