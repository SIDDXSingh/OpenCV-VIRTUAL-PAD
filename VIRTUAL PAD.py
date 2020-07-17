#import modules
import cv2
import numpy as np

#create Trackbar for color and other things
def n(x):
    print(x)
    return


st="Colurs And Other tools"
cv2.namedWindow(st)
cv2.createTrackbar("BLUE",st,0,255,n)
cv2.createTrackbar("RED",st,0,255,n)
cv2.createTrackbar("GREEN",st,0,255,n)
cv2.createTrackbar("BRUSH SIZE",st,1,50,n)
cap = cv2.VideoCapture(0)
#get the dimensions of the frame. To be used for making white canvas
w=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h= int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#Creating a white canvas
pad=255*np.ones((h,w,3),np.uint8)

x1 = -1
y1 = -1
while(1):


    # Take each frame
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)

    b=cv2.getTrackbarPos("BLUE",st)
    g=cv2.getTrackbarPos("GREEN",st)
    r=cv2.getTrackbarPos("RED",st)
    bs=cv2.getTrackbarPos("BRUSH SIZE",st)




    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # define range of red color in HSV
    lower_red = np.array([0, 152, 152])
    upper_red = np.array([15, 255, 255])
    # Threshold the HSV image to get only red colors
    ths = cv2.inRange(hsv, lower_red, upper_red)



    # Bitwise-AND mask and original image
    l1=cv2.adaptiveThreshold(ths,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,21,3)
    res2= cv2.bitwise_and(frame, frame, mask=l1)

    #find contours of the edges
    contours, hierarchy = cv2.findContours(l1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) != 0:
    #Since there may be many contours we can consider the contour of stylus to be of maximum area
        cnt = max(contours, key=cv2.contourArea)
        M = cv2.moments(cnt)

        #Centroid of the Contours of the edges.
        if (M['m00'] != 0):
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])

        #Minimum Enclosing Circle for the bounding the object
        (x, y), radius = cv2.minEnclosingCircle(cnt)
        center = (int(x), int(y))
        radius = int(radius)
        frame = cv2.circle(frame, center, radius, (0, 255, 0), 2)
        frame = cv2.circle(frame, center, radius // 10, (0, 255, 0), -1)


        #x1 and y1 are the former coordinates. And centre or x,y are the present coordinates.
        #These help in tracking the object and also in drawing free hand shape.
        if (x1 != -1 and y1 != -1):
            pad = cv2.line(pad, (x1, y1), center, (b, g, r), bs)
        x1 = int(x)
        y1 = int(y)

    #In case object suddenly disappears from current location and appears at a new location.
    if (len(contours) == 0):
        x1 = -1
        x2 = -1

    cv2.imshow('l[1]', frame)
    cv2.imshow(st,pad)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break


        
cv2.destroyAllWindows()