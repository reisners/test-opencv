import numpy as np
import cv2 as cv
cap = cv.VideoCapture(1)
out_send = cv.VideoWriter('appsrc ! ffmpegcolorspace ! "video/x-raw-yuv,format=(fourcc)YUY2" ! appsink name=GStreamSink caps=video/x-raw,format=RGB,width=160,pixel-aspect-ratio=1/1',cv.CAP_GSTREAMER,0, 20, (320,240), True)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the resulting frame
    out_send.write(frame)
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()