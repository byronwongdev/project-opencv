import cv2

# set the Graphics display resolution
frameWidth = 1600
frameHeight = 900
cap = cv2.VideoCapture("Resources/cars3.mp4")


while True:
    success, img = cap.read()
    img = cv2.resize(img, (frameWidth, frameHeight))
    
    ## xml  classifier
    classifier = "Resources/cars.xml"

    #create the tracker
    car_tracker = cv2.CascadeClassifier(classifier)

    ## convert to grey scale
    bnw = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    ## detect
    cars = car_tracker.detectMultiScale(bnw)

    ## draw rectangle
    for car in cars:
        (x,y,w,h) = car 
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)



    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break