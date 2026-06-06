import asyncio, os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
bot = Bot(token=os.getenv("BOT_TOKEN","YOUR_BOT_TOKEN_HERE"))
dp = Dispatcher()
@dp.message(CommandStart())
async def start(m): await m.answer("Привет!")
@dp.message()
async def echo(m): await m.answer(m.text)
async def main(): await dp.start_polling(bot)
if __name__=="__main__": asyncio.run(main())