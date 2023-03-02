from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

import db_lever as db

tg_bot_token = "5806634842:AAG0o0n3PFbddP-Ji05XHbi7lNqMTOKo5BE"


bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user_id = message.chat.id
    lever = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    up = types.KeyboardButton(text='Выкл')
    lever.add(up)
    db.lever_up()
    await bot.send_message(user_id, text='Вкл', parse_mode='HTML', reply_markup=lever)

@dp.message_handler(content_types = ['text'])
async def bot_lever(message: types.message):
    user_id = message.chat.id
    lever = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    up = types.KeyboardButton(text='Выкл')
    down = types.KeyboardButton(text='Вкл')
    text = message.text
    print(text)
    if text == "Вкл":
        db.lever_up()
        lever.add(up)


    elif text == "Выкл":
        db.lever_down()
        lever.add(down)
    await bot.send_message(user_id, text=text, parse_mode='HTML', reply_markup=lever)

executor.start_polling(dp, skip_updates=True)
db.conn.close()