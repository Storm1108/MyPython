from aiogram import *
import asyncio


def game_kb_create(game_data):
    game_kb = types.InlineKeyboardMarkup(row_width=3)
    button1 = types.InlineKeyboardButton(text=f'{game_data[0]}', callback_data='1')
    button2 = types.InlineKeyboardButton(text=f'{game_data[1]}', callback_data='2')
    button3 = types.InlineKeyboardButton(text=f'{game_data[2]}', callback_data='3')
    button4 = types.InlineKeyboardButton(text=f'{game_data[3]}', callback_data='4')
    button5 = types.InlineKeyboardButton(text=f'{game_data[4]}', callback_data='5')
    button6 = types.InlineKeyboardButton(text=f'{game_data[5]}', callback_data='6')
    button7 = types.InlineKeyboardButton(text=f'{game_data[6]}', callback_data='7')
    button8 = types.InlineKeyboardButton(text=f'{game_data[7]}', callback_data='8')
    button9 = types.InlineKeyboardButton(text=f'{game_data[8]}', callback_data='9')
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
