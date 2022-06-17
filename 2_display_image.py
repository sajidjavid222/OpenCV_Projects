import cv2

img = cv2.imread("C:\\Users\\Dell\\OneDrive\\Desktop\\OpenCV\\Sajid's\\Penguins.jpg",1)

cv2.imshow("Penguins",img)

# cv2.waitKey(0)

cv2.waitKey(2000)

cv2.destroyAllWindows()