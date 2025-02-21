import cv2
import time
import hand as htm
import math

cap = cv2.VideoCapture(0)
pTime = 0
detector = htm.handDetector(detectionCon=0.1)
while True:
    ret, frame = cap.read()
    #
    frame = detector.findHands(frame)
    lmList = detector.findPosition(frame, draw=False)
    if len(lmList):
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        # draw circle
        cv2.circle(frame, (x1, y1), 5, (255, 0, 0), -1)  # -1 : tròn đặc ruột
        cv2.circle(frame, (x2, y2), 5, (255, 0, 0), -1)  # -1 : tròn đặc ruột
        cv2.line(frame, (x1, y1), (x2, y2), (255, 0, 0), 3)
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
        cv2.circle(frame, (cx, cy), 5, (255, 0, 0), -1)
        len_vl = math.hypot(x2 - x1, y2 - y1)
        # 14- 155 ( min ,max)
        if len_vl < 14:
            cv2.circle(frame, (cx, cy), 10, (0, 0, 255), -1)
        print(len_vl)
    # FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(
        frame,
        f"FPS : {int(fps)}",
        (10, 70),
        cv2.FONT_HERSHEY_COMPLEX,
        1,
        (255, 255, 0),
        3,
    )
    cv2.imshow("volume", frame)
    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
