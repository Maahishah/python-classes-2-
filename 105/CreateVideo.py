import os
import cv2


path = "Images"

images = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)
        
#print(len(images))
count = len(images)
#print(count)

frame = cv2.imread(images[0])
cv2.imshow("Photo",frame)
#cv2.waitKey(6000)

height, width, channels = frame.shape
size = (width,height)
#print(size)

out = cv2.VideoWriter('sun.mp4',cv2.VideoWriter_fourcc(*'DIVX'), 10, size)

#For SUNSET
#for i in range(0,count-1 ,1):


#For SUNRISE
for i in range(count-1,0,-1):
    frame = cv2.imread(images[i])
    out.write(frame)
    
out.release() # releasing the video generated
print("Done")
