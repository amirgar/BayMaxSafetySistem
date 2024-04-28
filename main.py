from ai.get_photos import get_photos
from ai.check_warnings import check_warnings


if __name__ == "__main__":
    name = 'photo'
    path = rf'C:\Users\Airat\PycharmProjects\BayMax_Bank\ai\photo'
    counter = 3
    get_photos(path=path, name=name, counter=counter, timer=0.5)
    counter_angry = 0
    counter_fear = 0
    counter_old = 0
    for i in range(1, counter + 1):
        file = rf'{path}\photo{str(i)}.png'
        print(file)
        if check_warnings(img_path=file) == "Dangerous emoji: fear":
            counter_fear += 1
        if check_warnings(img_path=file) == "Dangerous emoji: angry":
            counter_angry += 1
        if check_warnings(img_path=file) == "Dangerous: old user":
            counter_old += 1
    print(f'Показатели страха: {counter_fear}')
    print(f'Показатели злости: {counter_angry}')
    print(f'Показатели старости: {counter_old}')
