import cv2
import numpy as np

def nothing(x):
    pass

img = np.zeros((300,512,3),np.uint8)
cv2.namedWindow("image")

cv2.createTrackbar("R","image",0,255,nothing) 
cv2.createTrackbar("G","image",0,255,nothing)
cv2.createTrackbar("B","image",0,255,nothing) 
#createTrackbar içine 4 parametre alır.
#Önce tanım ve nerede işlem göreceği yazılır.
#Daha sonra kaçtan kaça kadar gideceği yazılır. (0,255)
#İhtiyacımız olan her şeyi yazdıktan sonra son parametre boş kalır.
#Bu parametreden hata almamak için nothing fonksiyonu üretilir.
cv2.createTrackbar("ON/OFF","image",0,1,nothing) 

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    r = cv2.getTrackbarPos('R','image')
    g = cv2.getTrackbarPos('G','image')
    b = cv2.getTrackbarPos('B','image')
    s = cv2.getTrackbarPos('ON/OFF','image')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [r,g,b]

cv2.destroyAllWindows()
