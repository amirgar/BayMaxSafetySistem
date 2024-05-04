from cv2 import VideoCapture, imshow, imwrite


def get_photo(path=r'C:\Users\Airat\PycharmProjects\BayMax_Bank\ai\photos', name='photo', show=False) -> bool:
    cam = VideoCapture(0)
    result, image = cam.read()
    if result:
        if show:
            imshow("Photo", image)
        print(rf"{path}\{name}.png")
        imwrite(rf"{path}\{name}.png", image)
        return True
    else:
        return False


if __name__ == "__main__":
    get_photo()
