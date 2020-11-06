import cv2
import numpy as np

frameWidth = 1280
frameHeight = 720
cap = cv2.VideoCapture(1)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)

# h_min,s_min,v_min,h_max,s_max,v_max
#if you want to detect more colour add to the list 

mycolours = [[167,127,0,179,230,255],[24,84,84,49,134,196],[108,45,181,179,171,210]]

#the drawing colour BGR
mycoloursvalues = [[204,153,255],
[102,255,255],[204,153,255]]

mypoints = [] ##[x,y,colorId]

def findColour(img,mycolours,mycoloursvalues):
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    count = 0
    newpoint = []
    for color in mycolours:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV,lower,upper)
        x,y = getContours(mask)

        #drawing the circle on the top of the object
        cv2.circle(imgResult,(x,y),10,mycoloursvalues[count],cv2.FILLED)
        if x != 0 and y != 0:
            newpoint.append([x,y,count])
        count += 1

        #cv2.imshow(str(color[0]),mask)
    return newpoint

# kwang kwang for the object
def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>500:
            #cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            x, y, w, h = cv2.boundingRect(approx)
    return x+w//2,y

#### to draw on the canvas
def drawoncanvas(mypoints,mycoloursvalues):
    for point in mypoints:
        cv2.circle(imgResult,(point[0],point[1]),10,mycoloursvalues[point[2]],cv2.FILLED)

while True:
    success, img = cap.read()
    imgResult = img.copy()
    newpoint = findColour(img, mycolours,mycoloursvalues)
    
    if len(newpoint) != 0:
        for newp in newpoint:
            mypoints.append(newp)
    
    if len(mypoints) != 0:
        drawoncanvas(mypoints,mycoloursvalues)

    findColour(img,mycolours,mycoloursvalues)
    cv2.imshow("Result", imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break