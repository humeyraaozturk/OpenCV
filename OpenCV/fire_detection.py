import cv2

fire_cascade = cv2.CascadeClassifier('fire_detection.xml')
cap = cv2.VideoCapture(0)
counter = 0

while (counter == 0):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    fire = fire_cascade.detectMultiScale(frame,1.2,3)

    for (x,y,w,h) in fire:
        cv2.rectangle(frame,(x-20,y-20),(x+w+20,y+h+20),(255,0,0),2)
        roi_gray = gray[y:y+h,x:x+w]
        roi_color = frame[y:y+h,x:x+w]
        print("Ateş Tespit Edildi!")
        counter += 1
        cv2.imwrite('tespit_edilen_ates'+str(counter)+'.jpg',frame)



    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
