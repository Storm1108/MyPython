import datetime
import logging
from keyboards import calc_kb
from config_reader import config
from database_control import *
from functions import *

logging.basicConfig(level=logging.INFO, filename='log.csv')

bot = Bot(token=config.bot_token.get_secret_value())
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    name = message.from_user.first_name
    await message.reply(f"Привет, {name}!\n"
                        "Я бот сделанный по заданию ГикБрейнс\n"
                        "Список доступных команд:\n"
                        "/help - Просмотр списка всех команд заного\n"
                        "/game - запуск игры в крестики-нолики\n")


@dp.message_handler(commands=['game'])
async def crosses(message: types.Message):
    u_id = int(message.from_user.id)
    u_name = str(message.from_user.first_name)
    game_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 0, chr(10060)]
    logging.info(f'Начало игры-{datetime.datetime.now()}-{u_id}-{u_name}-{game_data}')
    await bot.send_message(chat_id=message.chat.id, text=f'Выберите позицию для {game_data[11]}',
                           reply_markup=game_kb_create(game_data))
    data_change_game(u_id, u_name, game_data)


@dp.message_handler(commands=['calc'])
async def calculator(msg: types.Message):
    value = ''
    data_change_calc(msg.from_user.id, msg.from_user.first_name,value)
    await bot.send_message(chat_id=msg.chat.id, text='Добро пожаловать в калькулятор', reply_markup=calc_kb)

@dp.callback_query_handler()
async def callback_func(query):
    data = query.data
    if data[0] == 'g':
        await game(query, bot)
    else:
        u_id = query.from_user.id
        u_name = query.from_user.first_name
        value = export_calc(u_id)
        if data == 'no':
            pass
        elif data == 'C':
            value = ''
        elif data == '<=':
            value = value[:len(value)-1]
        elif data == '=':
            try:
                logging.info(f'Попытка операции-{datetime.datetime.now()}-{u_id}-{u_name}-{value}')
                value = str(eval(value))
            except ZeroDivisionError:
                value = 'Ошибка'
            logging.info(f'Результат-{datetime.datetime.now()}-{u_id}-{u_name}-{value}')
        else: value += data
        if value == '':
            await bot.edit_message_text(text=f'0', chat_id=query.message.chat.id,
                                        message_id=query.message.message_id, reply_markup=calc_kb)
        elif 'Ошибка' in value:
            await bot.edit_message_text(text=f'{value}', chat_id=query.message.chat.id,
                                        message_id=query.message.message_id, reply_markup=calc_kb)
            value = ''
        else:
            await bot.edit_message_text(text=f'{value}', chat_id=query.message.chat.id,
                                        message_id=query.message.message_id, reply_markup=calc_kb)
        data_change_calc(u_id, u_name, value)
async def main():
    await dp.start_polling(bot)
