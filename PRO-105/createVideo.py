import os
import cv2
path = "Images/"
images = []

for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)

count = len(images)

frame = cv2.imread(images[0])
cv2.imshow("Photo",frame)
height, width, channels = frame.shape
size = (width,height)


out = cv2.VideoWriter('Project Video.mp4',cv2.VideoWriter_fourcc(*'DIVX'), 2, size)
for i in range(count-1,0,-1):
    frame = cv2.imread(images[i])
    out.write(frame)
    
out.release() # releasing the video generated
print("Done")


