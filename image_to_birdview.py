import cv2
import numpy as np

# store cordinates of click in array using numpy
array = np.zeros((4,2),int)

count = 0
# Function detects mouse letf click
def click(event, x, y, flags, parameters):
    global count
    if event == cv2.EVENT_LBUTTONDOWN: # if left button is press the cordinates will print
        cv2.circle(img, (x,y), 5, [0,255,0], -1) # draw point on the location of click
        array[count] = x,y 
        count += 1
        print(x,y)
        
width, height = 250,350 

# Reading source imageR
img = cv2.imread("cards.png")

while True:

    if count == 4:
        p1 = np.float32([array[0], array[1], array[2], array[3]])
        p2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
        matrix = cv2.getPerspectiveTransform(p1,p2)
        imgOut = cv2.warpPerspective(img, matrix, (width,height))
        cv2.imshow("Output", imgOut)
        if cv2.waitKey(0):
            break

    # Defining window name
    cv2.namedWindow("Source Img")

    # Calls the click function
    cv2.setMouseCallback("Source Img", click)

    cv2.imshow("Source Img", img)
    cv2.waitKey(1)
