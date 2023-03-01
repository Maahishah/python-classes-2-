import numpy as np
import cv2
#displaying the red image

red_img = cv2.imread("red.png")
#red2Grey_image = cv2.cvtColor(red_img,cv2.COLOR_RGB2GRAY)

#display the colored image
#cv2.imshow("Display Image", red_img)
#red_img = np.zeros([600,600])
red2Grey_image = np.zeros([800,800])
#red3d = np.zeros([5,5],[5,5],[5,5])


#cv2.imshow("Display Gray scale Image", red2Grey_image)
#$print(red_img)
#print(red2Grey_image)


#f_row = red2Grey_image[1:2]
#print(f_row)

#f_col = red2Grey_image[:,1:2]
#print(f_col)

#red2Grey_image[200:600,200:600] = 225
#print(red2Grey_image)

#cv2.imshow("red2Grey_image",red2Grey_image)

# import required libraries import cv2 import numpy as np 
# create a black image 
red_img = np.zeros((350, 700, 3), dtype = np.uint8) 
# display the image using opencv 
cv2.imshow('black image', red_img) 
cv2.waitKey(0)
print(red_img)

#cv2.waitKey(6000)