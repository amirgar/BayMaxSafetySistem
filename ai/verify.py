import cv2
from deepface import DeepFace
import matplotlib.pyplot as plt


def verify(img1_path, img2_path) -> str:
    img1 = cv2.imread(img1_path)
    img2 = cv2.imread(img2_path)

    fig = plt.figure(figsize=(10, 7))
    rows = 1
    columns = 2

    fig.add_subplot(rows, columns, 1)

    plt.imshow(img1[:, :, ::-1])
    plt.axis('off')
    plt.title('First')
    fig.add_subplot(rows, columns, 2)

    plt.imshow(img2[:, :, ::-1])
    plt.axis('off')
    plt.title('Second')
    plt.show()
    output = DeepFace.verify(img1_path, img2_path)
    print(output)
    verification = output['verified']
    if verification:
        return 'They are same'
    else:
        return 'The are not same'

if __name__ == "__main__":
    pass