import cv2

img = cv2.imread("C:\\Users\\Dell\\OneDrive\\Desktop\\OpenCV\\Sajid's\\Penguins.jpg",1)


half_resized = cv2.resize(img, (int(img.shape[1]/2),int(img.shape[0]/2)))

cv2.imshow("Penguins",half_resized)


# double_resized = cv2.resize(img, (int(img.shape[1]*2),int(img.shape[0]*2)))

# cv2.imshow("Penguins",double_resized)


cv2.waitKey(0)

cv2.destroyAllWindows()