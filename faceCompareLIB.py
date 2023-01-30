import cv2
import face_recognition

first = face_recognition.load_image_file('newImg1.jpg')
first = cv2.cvtColor(first, cv2.COLOR_BGR2RGB)
enc = face_recognition.face_encodings(first)[0]

second = face_recognition.load_image_file('newImg2.jpg')
second = cv2.cvtColor(second, cv2.COLOR_BGR2RGB)
enc2 = face_recognition.face_encodings(second)[0]

result = face_recognition.compare_faces([enc], enc2)
print("Face Match : ", result)

f = open("result.txt", "w")
f.write(result)
f.close()