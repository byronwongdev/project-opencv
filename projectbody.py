import cv2

# set the Graphics display resolution
frameWidth = 960
frameHeight = 540


cap = cv2.VideoCapture("Resources/people2.mp4")

#front camera
#cap = cv2.VideoCapture(1)


while True:
    success, img = cap.read()
    img = cv2.resize(img, (frameWidth, frameHeight))
    
    ## xml  classifier
    fullbody_classifier = "Resources/haarcascade_fullbody.xml"
    lowerbody_classifier = "Resources/haarcascade_lowerbody.xml"
    upperbody_classifier = "Resources/haarcascade_upperbody.xml"

    #create the tracker
    fullbody_tracker = cv2.CascadeClassifier(fullbody_classifier)
    lowerbody_tracker = cv2.CascadeClassifier(lowerbody_classifier)
    upperbody_tracker = cv2.CascadeClassifier(upperbody_classifier)

    ## convert to grey scale
    bnw = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    ## detect
    fullbodies = fullbody_tracker.detectMultiScale(bnw, 1.3, 5)
    lowerbodies = lowerbody_tracker.detectMultiScale(bnw, 1.3, 5)
    upperbodies = upperbody_tracker.detectMultiScale(bnw,1.3,5)

    ## draw rectangle
    for fullbody in fullbodies:
        (x,y,w,h) = fullbody 
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

    for lowerbody in lowerbodies:
        (x,y,w,h) = lowerbody 
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)

    for upperbody in upperbodies:
        (x,y,w,h) = upperbody
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

    



    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break