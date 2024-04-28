import time
from ai.get_photo import get_photo


""" 
path - путь к папке
name -  названия сделанных фоток в папке
counter - количество сделанных фоток
timer - интервал 
Если функция возвращает True, то функция успешно окончила работу, иначе - возникли ошибки
"""


def get_photos(path=r'C:\Users\Airat\PycharmProjects\BayMax_Bank\ai\photo', name='photo', counter=5, timer=1.5) -> bool:
    try:
        for i in range(1, counter + 1):
            get_photo(path, f'{name}{i}')
            time.sleep(timer)
        return True
    except:
        return False


if __name__ == "__main__":
    get_photos()
