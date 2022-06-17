 #importing the OpenCV module
import cv2

#method to create video capturing object which will trigger the camera
cap = cv2.VideoCapture(0)

#setting the width and height of the frame
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

#using while loop for continuous display of frames untill break condition
while True:
    #frame is a Numpy array representing first image that VideoCaptures
    #_ is a bool data type that returns true if python reads VideoCapture object
    _, frame = cap.read()
    
    #converting our frame from RGB model to HSV model
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    #frame.shape retuns a tuple (r,c,ch)
    #rows, columns and channels of frame assigned to height, width and _ resp.
    height, width, _ = frame.shape

    #getting the coordinates of the centre of frame
    cx = int(width / 2)
    cy = int(height / 2)
    
    # Picking pixel at the centre of the HSV frame
    pixel_center = hsv_frame[cy, cx]
    
    #Picking the hue value out of HSV (Hue, Saturation and value)
    hue_value = pixel_center[0]

    #color detection for different hue values
    if (hue_value < 7 or 175 < hue_value < 179):
        color = "RED"
    elif hue_value < 22:
        color = "ORANGE"
    elif hue_value < 33:
        color = "YELLOW"
    elif (33 < hue_value < 78) :
        color = "GREEN"
    elif hue_value < 131:
        color = "BLUE"
    elif hue_value < 170:
        color = "VIOLET"
    else:
        color = "RED"
        
    # Picking pixel at the centre of the frame
    pixel_center_bgr = frame[cy, cx]
    
    #storing the RBG values at centre of the frame in b,g,r
    b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])
    
    #placing a rectangular section , text varying color and circle detecting color on the frame
    cv2.rectangle(frame, (cx - 220, 10), (cx + 200, 120), (255, 255, 255), -1)
    cv2.putText(frame, color, (cx - 200, 100), 0, 3, (b, g, r), 5)
    cv2.circle(frame, (cx, cy), 5, (25, 25, 25), 3)
    
    #method for displaying the frame
    cv2.imshow("Frame", frame)
    
    #shows the output for 1 milliseconds but for infinite while loop it outputs
    #sequence of images
    key = cv2.waitKey(1)
    
    #window will be destroyed on pressing the key 27
    if key == 27:
        break
    
#release the VideoCapture object
cap.release()

#close all the windows currently opened
cv2.destroyAllWindows()





