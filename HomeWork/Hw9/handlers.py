import datetime
import logging
from config_reader import config
from functions import *
from database_control import *

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
    data_change(u_id, u_name, game_data)

@dp.callback_query_handler()
async def callback_func(query):
    way = query.data
    u_id = query.from_user.id
    u_name = query.from_user.first_name
    game_data = export(u_id)
    game_data = make_step(game_data, way)
    game_data = check(game_data)
    if game_data[9] != 9 and game_data[9] != 0:
        logging.info(f'Конец игры-{datetime.datetime.now()}-{u_id}-{u_name}-{game_data}')
        await bot.edit_message_text(text=f'Победили {game_data[11]}! Поздравляю!!', chat_id=query.message.chat.id,
                                    message_id=query.message.message_id,
                                    reply_markup=game_kb_create(game_data))
        game_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 0, chr(10060)]
    elif game_data[9] == 0:
        await bot.edit_message_text(text=f'Победила Дружба! Ничья!', chat_id=query.message.chat.id,
                                    message_id=query.message.message_id,
                                    reply_markup=game_kb_create(game_data))
        logging.info(f'Конец игры-{datetime.datetime.now()}-{u_id}-{u_name}-{game_data}')
        game_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 0, chr(10060)]
    else:
        try:
            await bot.edit_message_text(text=f'Выберите позицию для {game_data[11]}', chat_id=query.message.chat.id,
                                        message_id=query.message.message_id,
                                        reply_markup=game_kb_create(game_data))
            logging.info(f'Ход в игре-{datetime.datetime.now()}-{u_id}-{u_name}-{game_data}')
        except Exception:
            logging.info(f'Неверный ход-{datetime.datetime.now()}-{u_id}-{u_name}-{game_data[11]})')
    data_change(u_id, u_name, game_data)


async def main():
    await dp.start_polling(bot)



