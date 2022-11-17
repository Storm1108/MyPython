from aiogram import *
import asyncio
import logging
from config_reader import config
from functions import *

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.bot_token.get_secret_value())
dp = Dispatcher(bot)
game_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 0, chr(10060)]


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
    global game_data
    game_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 0, chr(10060)]
    await bot.send_message(chat_id=message.chat.id, text=f'Выберите позицию для {game_data[11]}',
                           reply_markup=game_kb_create(game_data))


@dp.callback_query_handler()
async def callback_func(query):
    global game_data
    way = query.data
    if way.isdigit():
        game_data = make_step(game_data, way)
        game_data = check(game_data)
        if game_data[9] != 9 and game_data[9] != 0:
            await bot.edit_message_text(text=f'Победили {game_data[11]}! Поздравляю!!', chat_id=query.message.chat.id,
                                        message_id=query.message.message_id,
                                        reply_markup=game_kb_create(game_data))
            game_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 0, chr(10060)]
        elif game_data[9] == 0:
            await bot.edit_message_text(text=f'Победила Дружба! Ничья!', chat_id=query.message.chat.id,
                                        message_id=query.message.message_id,
                                        reply_markup=game_kb_create(game_data))
            game_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 0, chr(10060)]
        else:
            try:
                await bot.edit_message_text(text=f'Выберите позицию для {game_data[11]}', chat_id=query.message.chat.id,
                                            message_id=query.message.message_id,
                                            reply_markup=game_kb_create(game_data))
            except: Exception

    elif way == 'start_cross':
        game_data[11] = chr(10060)
    elif way == 'start_round':
        game_data[11] = chr(11093)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
