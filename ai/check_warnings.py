import cv2
from deepface import DeepFace


def check_warnings(EPS=50.0, img_path=r"C:\Users\Airat\PycharmProjects\BayMax_Bank\ai\photo\GAREEV AMIR.png") -> str:
    img = cv2.imread(img_path)
    analyze = DeepFace.analyze(img, enforce_detection=False)
    analyze = analyze[0]
    emotion = analyze['emotion']
    if emotion['fear'] >= EPS:
        return "Dangerous emoji: fear"
    if emotion['angry'] >= EPS:
        return "Dangerous emoji: angry"
    age = int(analyze['age'])
    if age >= 55:
        return "Dangerous: old user"
    return "No warnings"


if __name__ == "__main__":
    print(check_warnings())

