#!/usr/bin/env python
import numpy as np
import cv2 
#odczyt filmu ze sciezki
#captured_video = cv2.VideoCapture('/home/krzysztof/catkin_ws/src/hello_world/src/perception/camera/kule.mov')
#odczyt streama z kamery na zywo
captured_video = cv2.VideoCapture(0)
if not captured_video.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = captured_video.read()
    # if frame is read correctly ret is True
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #zmiana ksztatu 
    frame = cv2.resize(frame, (0,0), fx = 0.5, fy = 0.5)
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    
    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(25) == ord('q'):
        break
# When everything done, release the capture
captured_video.release()
cv2.destroyAllWindows()