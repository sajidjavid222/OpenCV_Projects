import cv2

img = cv2.imread("C:\\Users\\Dell\\OneDrive\\Desktop\\OpenCV\\Sajid's\\Penguins.jpg",1)

resized = cv2.resize(img, (450,300))

cv2.imshow("Penguins",resized)

cv2.waitKey(0)

cv2.destroyAllWindows()