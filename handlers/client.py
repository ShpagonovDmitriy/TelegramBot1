from aiogram import types, Dispatcher
from create_bot import bot
from keyboards import kb_client
# from aiogram.types import ReplyKeyboardRemove


# @dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Welcome to us', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Chat with bot over PS, write him:'
                            '\nhttps://t.me/my_test_simple_bot')

# @dp.message_handler(commands=['Режим_работы'])
async def command_open(message : types.Message):
    await bot.send_message(message.from_user.id, 'Круглосуточно')

# @dp.message_handler(commands=['Расположение'])
async def command_place(message : types.Message):
    await bot.send_message(message.from_user.id, 'Сосногорск') # reply_markup=ReplyKeyboardRemove()

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(command_open, commands=['Режим_работы'])
    dp.register_message_handler(command_place, commands=['Расположение'])