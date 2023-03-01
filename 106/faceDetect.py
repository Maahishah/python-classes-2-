import cv2

img = cv2.imread("boy.jpg")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#drawing rect
face = face_cascade.detectMultiScale(gray)
#print (face)
 
 
 
for (x,y,w,h) in face:
       #var,co ordinate,rect ,color, number of color combinations
       cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)  
       
cv2.imshow("face",img)
cv2.waitKey(0)

