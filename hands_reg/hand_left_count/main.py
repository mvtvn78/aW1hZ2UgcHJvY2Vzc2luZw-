import cv2
import time
import os
import hand as htm

cap = cv2.VideoCapture(0)
FolderPath = "Fingers"
lst = os.listdir(FolderPath)
lst_hand = []
for i in lst:
    image = cv2.imread(f"{FolderPath}/{i}")
    lst_hand.append(image)
pTime = 0
detector = htm.handDetector(detectionCon=0.1)
fingerIdLsts = [4, 8, 12, 16, 20]
while True:
    ret, frame = cap.read()
    #  add frame detector
    frame = detector.findHands(frame)
    lmList = detector.findPosition(frame, draw=False)  # detect 20 point hands
    # handle regconite hands
    fingers = []
    if len(lmList):
        # ngon cai
        if lmList[fingerIdLsts[0]][1] < lmList[fingerIdLsts[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
        #
        for fingerId in range(1, len(fingerIdLsts)):
            if (
                lmList[fingerIdLsts[fingerId]][2]
                < lmList[fingerIdLsts[fingerId] - 2][2]
            ):
                fingers.append(1)
            else:
                fingers.append(0)
        print(fingers)
    # count number
    numHands = fingers.count(1)
    # h,w,c (add frame) (0,1,2,3,4,5,-1)
    h, w, c = lst_hand[numHands - 1].shape
    # 132 -> h , w -> 109
    frame[0:h, 0:w] = lst_hand[numHands - 1]
    #  add text frame
    cv2.rectangle(frame, (0, 200, 150, 400), (255, 0, 0), -1)
    cv2.putText(
        frame, str(numHands), (30, 390), cv2.FONT_HERSHEY_COMPLEX, 3, (0, 255, 0), 3
    )
    # FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    # show fps
    cv2.putText(
        frame,
        f"FPS : {int(fps)}",
        (150, 70),
        cv2.FONT_HERSHEY_TRIPLEX,
        3,
        (255, 0, 0),
        3,
    )
    cv2.imshow("llala", frame)
    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
