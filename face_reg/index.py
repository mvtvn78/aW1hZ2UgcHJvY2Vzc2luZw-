import cv2

face_detect = cv2.CascadeClassifier("models\haarcascade_frontalface_default.xml")
img = cv2.imread("test\demo.jpg")
faces = face_detect.detectMultiScale(img, 1.3, 5)
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y, w, h), (0, 0, 255), 2)
    cv2.imshow("img", img)
cv2.waitKey(0)
