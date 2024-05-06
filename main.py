from ai.get_photo import get_photo
from ai.register_face import check_registration
from ai.check_warnings import check_warnings
from app.start_app import StartApp, run_startApp
from app.user_cabinet_app import UserCabinet, run_userCabinet
from bot.messenger_client import run_server
import sqlite3


def test_register():
    type = input("Если вы хотите зарегистрироваться введите Sign Up, иначе Sign In: ")
    if type == 'Sign Up':
        name = input('Введите ваше имя с оборотной стороны карты: ')
        print('Встаньте прямо перед камерой, она будет снимать вас в ближайшие 10 секунд')
        get_photo(path='ai/photo', name=name)
        print('Регистрация прошла успешно, скоро будет доступен личный кабинет')
    else:
        name = input('Введите ваше имя с оборотной стороны карты: ')
        print('Встаньте прямо перед камерой, она будет снимать вас в ближайшие 10 секунд')
        if check_registration(path='ai/photo', check_name=name):
            print('Вход прошел успешно, скоро будет доступен личный кабинет')
        else:
            print('Не удалось войти в аккаунт. Повторите операцию снова')


if __name__ == '__main__':
    check_warnings()
    print('Модель успешно загружена✅✅✅')
    while True:
        surname = run_startApp()
        if surname:
            print('Вход в аккаунт выполнен успешно✅✅✅')
            connection = sqlite3.connect('users.db')
            cursor = connection.cursor()
            result = cursor.execute("SELECT * FROM Users WHERE surname=?", (surname,)).fetchall()[0]
            # result -> name, surname, card, cvv, date
            connection.close()
            # print(result)
            run_userCabinet(result)
        else:
            print('Не удалось войти в аккаунт. Попробуйте войти снова❎❎❎')
            break
