import cv2
from deepface import DeepFace


def check_warnings(EPS=35.0, img_path=r"C:\Users\Airat\OneDrive\Desktop\WIN_20240426_19_28_47_Pro.jpg") -> str:
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

