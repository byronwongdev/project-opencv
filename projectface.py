import cv2

# set the Graphics display resolution
frameWidth = 1280
frameHeight = 720


#cap = cv2.VideoCapture("Resources/face2.mp4")

#front camera
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)


while True:
    success, img = cap.read()
    img = cv2.resize(img, (frameWidth, frameHeight))
    
    ## xml  classifier
    classifier = "Resources/haarcascade_frontalface_default.xml"

    #create the tracker
    face_tracker = cv2.CascadeClassifier(classifier)

    ## convert to grey scale
    bnw = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    ## detect
    faces = face_tracker.detectMultiScale(bnw)

    ## draw rectangle
    for face in faces:
        (x,y,w,h) = face 
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)



    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break