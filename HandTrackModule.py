import cv2
import mediapipe as mp
import time

class handdetector():
    def __init__(self,mode=False,maxhands=2,complexity=1,Mindetnconf=0.5,Mintrkconf=0.5):
        self.mode = mode
        self.maxhands = maxhands
        self.complexity = complexity
        self.Mindetnconf = Mindetnconf
        self.Mintrkconf = Mintrkconf

        # create an object to detect the hand

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode,self.maxhands,self.complexity,self.Mindetnconf,self.Mintrkconf)  # Object Hands-Default parameters are good for us
        self.mpDraw = mp.solutions.drawing_utils

    def findhands(self,img,draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # convert the image taken to RGB
        self.results = self.hands.process(imgRGB)  # Processes the image-Processes an RGB image and returns the hand landmarks and handedness of each detected hand
        # print(results.multi_hand_landmarks)
        # We have max 2 hands so using a for loop we try to traverse through them
        if self.results.multi_hand_landmarks:
            # handLms in one hand it could be hand 1 or hand 2
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms,self.mpHands.HAND_CONNECTIONS)  # Draws the dots and the lines for the hand
                    # We use the original img and not the RGB as we are displaying the orignal img and not the RGB one
        #To draw on img we have to return the img
        return img

    def findPosition(self,img,handNo=0,draw=True,color=(255, 0, 0)):
        lmList=[]
        if self.results.multi_hand_landmarks:
            myHand=self.results.multi_hand_landmarks[handNo]

            for id, lm in enumerate(myHand.landmark):
                # print(id,lm) #id is a pt on hand and lm is the actual (x,y,z) posn of theses id
                h, w, c = img.shape  # height width and channels are req as the lm are in decimals and thus ratio of w and h and need to be multiplied to get the pixel value
                cx, cy = int(lm.x * w), int(lm.y * h)
                # print(id, ":", cx, cy)
                lmList.append([id,cx,cy])
                if draw:
                    cv2.circle(img, (cx, cy),7, color, cv2.FILLED)


        return lmList

def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    detector=handdetector()
    while True:
        success, img = cap.read()
        img=detector.findhands(img)
        lmList=detector.findPosition(img)
        if len(lmList)!=0:
            print(lmList[0])#index is the point no.
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__=="__main__":
    main()