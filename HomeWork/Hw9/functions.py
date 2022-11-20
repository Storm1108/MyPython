import datetime
import logging
from keyboards import calc_kb
from aiogram import *

from database_control import *


def game_kb_create(game_data):
    game_kb = types.InlineKeyboardMarkup(row_width=3)
    button1 = types.InlineKeyboardButton(text=f'{game_data[0]}', callback_data='g1')
    button2 = types.InlineKeyboardButton(text=f'{game_data[1]}', callback_data='g2')
    button3 = types.InlineKeyboardButton(text=f'{game_data[2]}', callback_data='g3')
    button4 = types.InlineKeyboardButton(text=f'{game_data[3]}', callback_data='g4')
    button5 = types.InlineKeyboardButton(text=f'{game_data[4]}', callback_data='g5')
    button6 = types.InlineKeyboardButton(text=f'{game_data[5]}', callback_data='g6')
    button7 = types.InlineKeyboardButton(text=f'{game_data[6]}', callback_data='g7')
    button8 = types.InlineKeyboardButton(text=f'{game_data[7]}', callback_data='g8')
    button9 = types.InlineKeyboardButton(text=f'{game_data[8]}', callback_data='g9')
    game_kb.add(button1, button2, button3, button4, button5, button6, button7, button8, button9)
    return game_kb


def check(game_data):
    for i in range(3):
        if (game_data[i * 3] == game_data[i * 3 + 1] == game_data[i * 3 + 2]) or \
                (game_data[i] == game_data[i + 3] == game_data[i + 6]) or \
                (game_data[0] == game_data[4] == game_data[8]) or \
                (game_data[2] == game_data[4] == game_data[6]):
            if game_data[11] == chr(10060):
                game_data[11] = chr(11093)
            elif game_data[11] == chr(11093):
                game_data[11] = chr(10060)
            game_data[9] = game_data[11]
        elif game_data[10] >= 9:
            if game_data[11] == chr(10060):
                game_data[11] = chr(11093)
            elif game_data[11] == chr(11093):
                game_data[11] = chr(10060)
            game_data[9] = 0

    return game_data


def make_step(game_data, way):
    if game_data[int(way) - 1] != chr(10060) and game_data[int(way) - 1] != chr(11093):
        game_data[int(way) - 1] = game_data[11]
        game_data[10] += 1
        if game_data[11] == chr(10060):
            game_data[11] = chr(11093)
        elif game_data[11] == chr(11093):
            game_data[11] = chr(10060)
        return game_data
    return game_data


async def game(query, bot):
    data = query.data
    way = int(data[1:])
    u_id = query.from_user.id
    u_name = query.from_user.first_name
    game_data = export_game(u_id)
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
    data_change_game(u_id, u_name, game_data)

async def calc(query, bot, data):
    u_id = query.from_user.id
    u_name = query.from_user.first_name
    value = export_calc(u_id)
    if data == 'no':
        pass
    elif data == 'C':
        value = ''
    elif data == '<=':
        value = value[:len(value) - 1]
    elif data == '=':
        try:
            logging.info(f'Попытка операции-{datetime.datetime.now()}-{u_id}-{u_name}-{value}')
            value = str(eval(value))
        except ZeroDivisionError:
            value = 'Ошибка'
        logging.info(f'Результат-{datetime.datetime.now()}-{u_id}-{u_name}-{value}')
    else:
        value += data
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