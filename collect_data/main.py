import cv2
import os

folder_path = "F:\\Working\\DeepPhaKe\\df50k\\Dataset\\Validation\\Real"
face_detect = cv2.CascadeClassifier("models\haarcascade_frontalface_default.xml")
stt = 0
fileName = "real"
pathStore = f"datasets\\validation\\{fileName}\\"
size = 500
print("Start collecting data")
for root, dirs, files in os.walk(folder_path):
    for file in files:
        if stt > size:
            break
        full_path = os.path.join(root, file)
        img = cv2.imread(full_path)
        faces = face_detect.detectMultiScale(img, 1.3, 6)
        for x, y, w, h in faces:
            detect_face = img[y : y + h, x : x + w]
            ext = full_path.split(".")[-1]
            img_detect = cv2.resize(detect_face, (224, 224))
            storePath = f"{pathStore}{fileName}_{stt}.{ext}"
            cv2.imwrite(storePath, img_detect)
            print(f"Save {storePath}")
            stt += 1
        # if cv2.waitKey(0) & 0xFF == ord("q"):
        #     break
print("Finish collecting data")
