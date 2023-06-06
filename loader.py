import os
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from db import Db

load_dotenv()

token = os.getenv('TOKEN')
bot = Bot(token)
dp = Dispatcher(bot)

db = Db()