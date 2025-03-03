import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import Message, WebAppInfo

from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())


# Инициализация бота и диспетчера
bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    await message.answer(
        f"Твой ID: <code>{user_id}</code>\n"
        f"Чат ID: <code>{chat_id}</code>",
        parse_mode="HTML"
    )
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton("открыть сайт", web_app=WebAppInfo(url='')))
    await message.answer("привет", reply_markup=markup)



async def on_startup():
    """Действия при запуске бота."""
    print('Бот стартовал')



async def on_shutdown():
    """Действия при остановке бота."""
    print('Бот остановлен')


async def main():
    """Основная функция запуска бота."""
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    try:
        await dp.start_polling(bot)
    except Exception as e:
        print(f"Ошибка при запуске бота: {repr(e)}")
    finally:
        await bot.session.close()


if __name__ == '__main__':
    print('1')
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот остановлен вручную')