from ai.get_photo import get_photo
from ai.register_face import check_registration

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
