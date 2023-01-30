import cv2
import numpy as np
import time

TIMER = int(5)
message = "Please stay in the frame"
msg1 = "Also keep your Aadhar card in the frame"

# Open the camera
cap = cv2.VideoCapture(1)
cap2 = cv2.VideoCapture(0)

while True:
	
	# Read and display each frame
	ret, img = cap.read()
	cv2.imshow('Card', img)
	cv2.moveWindow('Card', 40,50)

	ret2, img2 = cap2.read()
	cv2.imshow('Face', img2)
	cv2.moveWindow('Face', 800,50)

	if True:
		prev = time.time()

		while TIMER >= 0:
			ret, img = cap.read()
			ret2, img2 = cap2.read()
			font = cv2.FONT_HERSHEY_SIMPLEX
			cv2.putText(img, str(message), (50, 80), font, 0.8, (0, 0, 0), 2, cv2.LINE_AA)
			cv2.putText(img, str(msg1), (50, 100), font, 0.8, (0, 0, 0), 2, cv2.LINE_AA)
			cv2.putText(img, str(TIMER), (200, 250), font, 3, ( 255, 0, 0), 4, cv2.LINE_AA)
			cv2.imshow('Card', img)
			cv2.imshow('Face', img2)
			cv2.waitKey(10)

			cur = time.time()

			if cur-prev >= 1:
				prev = cur
				TIMER = TIMER-1

		else:
			ret, img = cap.read()
			ret2, img2 = cap2.read()
			cv2.waitKey(1)
			cv2.imwrite('img2.jpg', img)
			cv2.imwrite('img1.jpg', img2)
			break

# close the camera
cap.release()
cap2.release()

# close all the opened windows
cv2.destroyAllWindows()

for i in [1,2]:
	img = "img" + str(i) + ".jpg"
	# HaarCascade file, to detect the face.
	faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
	image = cv2.imread(img)

	#Convert image to grayscale
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	grays = []
	faces = faceCascade.detectMultiScale(
		gray,
		scaleFactor=1.1,
		minNeighbors=5,
		minSize=(30, 30)
	)

	for (x,y,w,h) in faces:
		cv2.imwrite("newImg"+ str(i) + ".jpg", gray[y-20:y+h+20, x-20:x+w+20])
		cv2.waitKey(100)