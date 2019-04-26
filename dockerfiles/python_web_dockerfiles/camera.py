import numpy as np
import cv2

cap = cv2.VideoCapture(0)
cap.release()

webcap_url = "http://10.239.154.169:8090/camera.mjpeg"
webcap = cv2.VideoCapture(webcap_url)

while(True):

    ret, frame = webcap.read()
    if ret:
        print "receive frame from webcap.read()"
    	#cv2.imshow('frame',frame)
    else:
	print "cap.read() return false"
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcap.release()
cv2.destroyAllWindows()
