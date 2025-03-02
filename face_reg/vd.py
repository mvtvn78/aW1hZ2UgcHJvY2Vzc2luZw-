import cv2
import random

face_detect = cv2.CascadeClassifier("models\haarcascade_frontalface_default.xml")
video = cv2.VideoCapture(0)
while True:
    _, frame = video.read()
    faces = face_detect.detectMultiScale(frame, 1.3, 5)
    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y, w, h), (0, 0, 255), 1)
        detect_img = frame[y : y + h - 2, x : x + w - 2]
        cv2.imwrite(f"testing{random.randrange(1, 10, 1)}.png", detect_img)
    cv2.imshow("frame", frame)
    if cv2.waitKey(30) & 0xFF == ord("q"):
        break
video.release()
cv2.destroyAllWindows()
