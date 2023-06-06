import cv2
import mediapipe as mp
import time


cap=cv2.VideoCapture(0);
#Webcam No. 0

# create an object to detect the hand
mpHands=mp.solutions.hands
hands = mpHands.Hands()  #Object Hands-Default parameters are good for us

mpDraw=mp.solutions.drawing_utils


#for frame rate
pTime=0
cTime=0
while True:
    success,img = cap.read()
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)#convert the image taken to RGB
    results = hands.process(imgRGB) #Processes the image-Processes an RGB image and returns the hand landmarks and handedness of each detected hand
    #print(results.multi_hand_landmarks)
    # We have max 2 hands so using a for loop we try to traverse through them
    if results.multi_hand_landmarks:
        #handLms in one hand it could be hand 1 or hand 2
        for handLms in results.multi_hand_landmarks:
            for id,lm in enumerate(handLms.landmark):
                #print(id,lm) #id is a pt on hand and lm is the actual (x,y,z) posn of theses id
                h,w,c=img.shape#height width and channels are req as the lm are in decimals and thus ratio of w and h and need to be multiplied to get the pixel value
                cx,cy=int(lm.x*w),int(lm.y*h)
                print(id,":",cx,cy)
                if id==4:
                    cv2.circle(img,(cx,cy),15,(255,0,255),cv2.FILLED)
            #We use the original img and not the RGB as we are displaying the orignal img and not the RGB one
            mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)#Draws the dots and the lines for the hand


    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime

    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
    cv2.imshow("Image",img)
    cv2.waitKey(1)
