import hand_tracking_module as htm
import cv2
import time
import numpy as np
import math
import pulsectl

def adjust_vol(vol):
    with pulsectl.Pulse('volume-adjuster') as pulse:
        for sink in pulse.sink_list():
            # Volume is usually in 0-1.0 range, with >1.0 being soft-boosted
            pulse.volume_set_all_chans(sink, vol/100)

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = htm.handDetector(detectionCon=0.7)

vol = 0

ptime = 0

while True:
    success, img = cap.read()
    
    img= detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    
    if len(lmList) != 0:
        
        # tip of thumb and and index finger
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        cx, cy = (x1+x2)//2, (y1+y2)//2
        
        cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
        cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
        
        #length of line 
        length = math.hypot(x2-x1, y2-y1)
        if length<50:
            cv2.circle(img, (cx, cy), 15, (0, 255, 0), cv2.FILLED)
        
        vol = np.interp(length, [50, 280], [0, 100]) # this will give the volume in range of 0-100 by using the original range of length which is 50-280 
        adjust_vol(vol)
        
    # create volume bar
    cv2.putText(img, str(int(vol))+"%", (1190, 100), cv2.FONT_HERSHEY_PLAIN, 2,(255, 0, 255), 3)
    cv2.rectangle(img, (1200, 150), (1250, 550), (255, 0, 255), 3)
    cv2.rectangle(img, (1200, 400-int(vol*4)+150), (1250, 550), (0, 255, 0), cv2.FILLED)
    
    
    ctime = time.time()
    fps = 1/(ctime-ptime)
    ptime = ctime
    cv2.rectangle(img, (0, 0), (370, 100), (255, 255, 255), cv2.FILLED)
    cv2.putText(img, "FPS : " + str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 5,(255, 0, 255), 5)
    
    cv2.imshow("Image", img)
    cv2.waitKey(1)