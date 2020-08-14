# OpenCV-VIRTUAL-PAD
The basic principle used is **Object tracking via contours**.

In my code I have used red coloured objects(preferably bottle caps) as a stylus.

## Algorithm:
1. First we convert each frame from BGR to HSV as HSV colorspace is more suited for object tracking and extracting specific colours.
2. Now we declare the lower and upper rangers of red colour( lower_red = [0, 152, 152], upper_red = [15, 255, 255]) and then use cv2.inRange function to create a mask.
3. Now we threshhold this mask for more accuracy. We can also use morphological transformations for the same.
![alt text](https://github.com/SIDDXSingh/OpenCV-VIRTUAL-PAD/blob/master/Snippets/threshhold.PNG)


4. Then we find the contours in the mask.
5. There may be many contours present so we find the contour of maximum area whch is the contour of our object.


6. Now we find minimum bounding circle of the contours and its centre.

![alt text](https://github.com/SIDDXSingh/OpenCV-VIRTUAL-PAD/blob/master/Snippets/colour.PNG)


7. Now we just track the position of the centre in each frame correspondingly draw each point giving us a free curve or line.
 ![alt text](https://github.com/SIDDXSingh/OpenCV-VIRTUAL-PAD/blob/master/Snippets/Capture.PNG)
 
 
We can also add options like brush size etc. for better interface

