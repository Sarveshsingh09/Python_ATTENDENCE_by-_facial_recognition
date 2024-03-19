#code by sarvesh@2004
import csv
import face_recognition
import numpy as np 
import cv2
from datetime import datetime

video_capture = cv2.VideoCapture(0)

sarvesh_image = face_recognition.load_image_file("known_faces/Sarvesh.jpeg")
sarvesh_encoding = face_recognition.face_encodings(sarvesh_image)[0]

vishal_image = face_recognition.load_image_file("known_faces/vishal.jpg")
vishal_encoding = face_recognition.face_encodings(vishal_image)[0]

Files_faces = ["sarvesh","vishal"]
Files_faces_encoding=  [sarvesh_encoding,vishal_encoding]

students = Files_faces_name.copy()
faces_located = []
face_encodings =[]

# date time of face recognition
now = datetime.now()
current_date = now.strftime("%d-%m-%Y")

f = open(f"{current_date}.csv", "w+",newline="")
lnwriter = csv.writer(f)

while True:
    _,frame =  video_capture.read()
    small_frame = cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame,cv2.Color.BGR2RGB)
    
    faces_located = face_recognition.faces_located(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame,faces_located)
    
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces[Files_faces_encoding,face_encoding]
        face_distance = face_recognition.face_distance[Files_faces_encoding,face_encoding]
        best_match_index = np.argmin(face_distance)
         
        if (matches[best_match_index]):
            name=Files_faces_name[best_match_index]
        
        if name in Files_faces_encoding:
            font = cv2.FONT_HERSHEY_SIMPLEX
            bottomleftcorneroftext  = (10,100)
            fontscale = 1.5
            fontcolor = (255,0,0)
            thickness = 2
            linetype = 2
            cv2.putText(frame ,"wlecome ,"+name+" is present",bottomleftcorneroftext, font,fontScale,fontcolor,thickness,linetype)
        if name not in Files_faces_encoding:
            cv2.putText(frame ,"CHAL BE HAAWAA ANE DE INSHORT PHELI FURSAT MEI NIKAL" ,bottomleftcorneroftext, font,fontScale,fontcolor,thickness,linetype)
        if name in students:
            current_time= now.strftime("%H:%M:%S")
            lnwriter.writerow(name,current_time)
        
    cv2.imshow("attendence",frame)
    if cv2.waitKey(1)  & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()
f.close()
















#code by sarvesh@2004