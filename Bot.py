import asyncio
import logging
import python_weather
from aiogram import Bot, Dispatcher, types
import os
from dotenv import load_dotenv
from aiogram.filters import Command

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher()
@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "👋 Привет!\n\n"
        "Я бот погоды.\n"
        "Просто напиши название города, например:\n"
        "Seoul\n"
        "Bishkek\n"
        "London"
    )
@dp.message(Command("help"))
async def help_command(message: types.Message):
    await message.answer(
        "📖 Доступные команды:\n\n"
        "/start - запустить бота\n"
        "/help - помощь\n\n"
        "Для получения погоды просто отправь название города."
    )
@dp.message()
async def get_weather(message: types.Message):
    try:
        async with python_weather.Client(unit=python_weather.METRIC) as client:
            weather = await client.get(message.text)

            resp_msg = (
                f"🌍 Страна: {weather.country}\n"
                f"🏙 Город: {weather.location}\n"
                f"🌡 Температура: {weather.temperature}°C\n"
                f"🤗 Ощущается как: {weather.feels_like}°C\n"
                f"☁️ Погода: {weather.description}"
            )

            await message.answer(resp_msg)

    except Exception:
        await message.answer("❌ Город не найден.")
async def main():
    logging.basicConfig(level=logging.INFO)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
if __name__ == '__main__':
    asyncio.run(main())
