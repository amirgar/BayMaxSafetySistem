from config import TOKEN
import aiogram
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types import InputFile
import asyncio

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    await message.answer("Команда /image выведет фотки пользователя банкомата\n"
                         "Команда /user выведет имя и статистику пользователя")


@dp.message(Command('image'))
async def cmd_image(message: types.Message):
    for i in range(3):
        path = rf'C:\Users\Airat\PycharmProjects\BayMax_Bank\ai\photos\photo{i}.png'
        photo = types.FSInputFile(path=path)
        await bot.send_photo(chat_id=message.chat.id, photo=photo, caption=f'Номер фотографии: {i + 1}')


@dp.message(Command('user'))
async def cmd_user(message: types.Message):
    with open(r'C:\Users\Airat\PycharmProjects\BayMax_Bank\data_about_current_user.txt', 'r', encoding='utf-8') as file:
        text = file.read()
        await message.answer(text)


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    print("Bot's working has been started")
    asyncio.run(main())

