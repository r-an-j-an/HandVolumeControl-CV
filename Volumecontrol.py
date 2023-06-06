import cv2
import mediapipe as mp
import time
import numpy as np
import math
import HandTrackModule as htm
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)
# volume.GetMute()
# volume.GetMasterVolumeLevel()
volRange = volume.GetVolumeRange()
# volume.SetMasterVolumeLevel(-32.75,None)
print(volRange)
minvol = volRange[0]
maxvol = volRange[1]
vol=0
volbar=450
#######################################################
wCam, hCam = 640, 480
#######################################################

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0
cTime = 0
detector = htm.handdetector(Mindetnconf=0.5)
while True:
    success, img = cap.read()
    img = detector.findhands(img)  # remove default tracings of hand by draw=false as a param
    lmList = detector.findPosition(img, draw=False)  # remove custom drawings using draw=false and color as you like
    if len(lmList) != 0:
        thumbtip = lmList[4]
        indextip = lmList[8]
        x1, y1 = thumbtip[1], thumbtip[2]
        x2, y2 = indextip[1], indextip[2]
        distance = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))
        cv2.circle(img, (x1, y1), 10, (0, 255, 0), cv2.FILLED)
        cv2.circle(img, (x2, y2), 10, (0, 255, 0), cv2.FILLED)

        cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 5)
        cv2.circle(img, ((x1 + x2) // 2, (y1 + y2) // 2), 10, (0, 255, 0), cv2.FILLED)
        # print(distance)
        minlen = 0
        maxlen = 190
        minlimit=15
        if distance>maxlen:
            distance=maxlen
        if distance<minlimit:
            distance=minlen
        cv2.putText(img, str(int(distance * 100 / maxlen-minlen)), (35, 130), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
        vol = np.interp(distance * 100 / maxlen-minlen, [0, 100], [minvol, maxvol])
        volbar = np.interp(distance * 100 / maxlen-minlen, [0, 100], [450, 150])
        volume.SetMasterVolumeLevel(vol, None)
        cv2.rectangle(img,(50,150),(85,450),(0,255,0),3)
        if distance==maxlen:
            cv2.rectangle(img,(50,int(volbar)),(85,450),(0,0,255),cv2.FILLED)
            cv2.rectangle(img,(50,150),(85,450),(0,0,255),3)
            cv2.circle(img, (x1, y1), 10, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x2, y2), 10, (0, 0, 255), cv2.FILLED)
            cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 5)
            cv2.circle(img, ((x1 + x2) // 2, (y1 + y2) // 2), 10, (0, 255, 255), cv2.FILLED)
        elif distance == minlen:
            cv2.rectangle(img, (50, 150), (85, 450), (0, 255, 255), 3)
            cv2.circle(img, ((x1 + x2) // 2, (y1 + y2) // 2), 12, (0, 255, 255), cv2.FILLED)
        else:
            cv2.rectangle(img,(50,int(volbar)),(85,450),(0,255,0),cv2.FILLED)
        print(vol)


    # print(lmList[4],lmList[8])  # index is the point no.
    cv2.imshow("Volume Control", img)
    cv2.waitKey(1)
