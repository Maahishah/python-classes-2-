import cv2
solar = cv2.imread("solar-system.jpg")
cv2.imshow("output",solar)

cv2.waitKey(0)
print(solar)