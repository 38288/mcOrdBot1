from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import Message, WebAppInfo
import os
from dotenv import find_dotenv, load_dotenv
import asyncio

# Загрузка переменных окружения
load_dotenv(find_dotenv())

# Инициализация бота и диспетчера
bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    # Создаем клавиатуру с кнопкой для открытия Web App
    markup = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="Открыть сайт", web_app=WebAppInfo(url='https://www.google.com'))]
        ],
        resize_keyboard=True  # Делаем клавиатуру компактной
    )

    # Отправляем сообщение с клавиатурой
    await message.answer("Привет! Нажми на кнопку ниже, чтобы открыть сайт.", reply_markup=markup)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())