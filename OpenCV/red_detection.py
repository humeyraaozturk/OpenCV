import cv2
import numpy as np

cap = cv2.VideoCapture(r"D:\xyz\hüm\UAV_Task\serit.mp4")


object_detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=40) 
#Nesneleri renk kategorisine göre algılar

while True:
    ret, frame = cap.read()
    height, width, _ = frame.shape
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    sensitivity = 15
    lower_red = np.array([160,100,100])
    upper_red = np.array([179,255,255])
    mask = cv2.inRange(hsv,lower_red,upper_red)
    res = cv2.bitwise_and(frame,frame,mask = mask)
    
    roi = frame[440: 720,500: 1200]
    #İlgilenilen alan

    mask = object_detector.apply(roi)
    
    contours, _ = cv2.findContours(mask,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)   

    for c in contours:
        area =cv2.contourArea(c)
        if area > 2000:
            x, y, w, h = cv2.boundingRect(c)
            #dikdörtgen çizimi

            cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 255, 0), 3)

    cv2.imshow("Frame", frame)
    cv2.imshow("sonuc",res)
    cv2.imshow("Mask", mask)

    key = cv2.waitKey(30)
    if key == 27:
        break 

cap.release()
cv2.destroyAllWindows()
