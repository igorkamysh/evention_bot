import logging
import random

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5926163568:AAHgteMtLgz9G3Tdide13aXaDGTG252xRkY'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Привет!\nЯ помогу тебе найти, чем заняться!")

@dp.message_handler(commands=['find'])
async def echo(message: types.Message):
    fr = open("0"+ str(random.randint(1, 4)) +'.txt', 'r')
    data = ''.join(fr.readlines())
    await message.answer(data)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)