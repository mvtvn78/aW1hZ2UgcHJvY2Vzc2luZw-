import cv2

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    print(ret)
    # True : qua trinh doc oke
    # False : camera bi mat so huu
    cv2.imshow("sss", frame)
    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
