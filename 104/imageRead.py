import cv2


#Read Image
img = cv2.imread("butterfly.jpg")

grey_img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

# display the colored image
#cv2.imshow("Display Image", img)


cv2.imshow("Display Gray scale Image", grey_img)
#print(img)
print(grey_img)

cv2.waitKey(6000)


