from http.client import responses
import asyncio
import logging
import python_weather
from aiogram import Bot, Dispatcher, types
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher()
@dp.message()
async def get_weather(message: types.Message):
    async with python_weather.Client(unit=python_weather.METRIC) as client:
        weather = await client.get(message.text)
        resp_msg = f"{weather.country}\n"
        resp_msg += f"{weather.temperature}\n"
        resp_msg += f"{weather.feels_like}"
        await message.answer(resp_msg)
        # except:
        #     await message.answer("Undefined City")
async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)
if __name__ == '__main__':
    asyncio.run(main())