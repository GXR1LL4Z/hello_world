#!/usr/bin/env python
import numpy as np
import cv2 
captured_video = cv2.VideoCapture(0)
if not captured_video.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = captured_video.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    
    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
captured_video.release()
cv2.destroyAllWindows()