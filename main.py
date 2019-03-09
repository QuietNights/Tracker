import numpy as np
import cv2 as cv


def imageCircleDetect():
    image = cv.imread('garbage.png')
    image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    circles = cv.HoughCircles(image, cv.HOUGH_GRADIENT, 1, 40, param1=50, param2=30, minRadius=1, maxRadius=0)
    circles = np.uint16(np.around(circles))
    image = cv.cvtColor(image, cv.COLOR_GRAY2BGR)
    for i in circles[0,:]:
        cv.circle(image, (i[0], i[1]), i[2], (0,255,0),2)
        cv.circle(image,(i[0],i[1]),2,(0,0,255),3)
    cv.imshow('gang', image)
    print(len(circles))

def videoCircleDetect():

    cap = cv.VideoCapture('media/video/tracking-example.mp4')
    
    while(cap.isOpened()):
        
        ret, frame = cap.read()
        frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        circles = cv.HoughCircles(frame, cv.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=40, maxRadius=60)
        frame = cv.cvtColor(frame, cv.COLOR_GRAY2BGR)
        
        if circles is not None:
            circles = np.uint16(np.around(circles))        
            for i in circles[0,:]:
                cv.circle(frame,(i[0],i[1]),i[2],(0,255,0),2)
            
        cv.imshow('frame', frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()

videoCircleDetect()
