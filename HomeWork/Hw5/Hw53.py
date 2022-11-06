def field_paint(game_data):
    print(10 * '\n')
    print(
        f"\n"
        f"---------------------\n"
        f"  {game_data[0]}      {game_data[1]}      {game_data[2]}\n"
        f"---------------------\n"
        f"  {game_data[3]}      {game_data[4]}      {game_data[5]}\n"
        f"---------------------\n"
        f"  {game_data[6]}      {game_data[7]}      {game_data[8]}\n"
        f"---------------------\n")


def enter(game_data, player):
    while True:
        way = input(f'Выберите позицию для {player}')
        if way.isdigit() and 1 <= int(way) <= 9:
            if game_data[int(way) - 1] != chr(10060) and game_data[int(way) - 1] != chr(11093):
                game_data[int(way) - 1] = player
                return game_data
            else:
                field_paint(game_data)
                print('Эта клетка уже занята')
        else:
            field_paint(game_data)
            print('Введите число от 1 до 9')


def check(game_data, player):
    for i in range(3):
        if (game_data[i * 3] == game_data[i * 3 + 1] == game_data[i * 3 + 2]) or \
                (game_data[i] == game_data[i + 3] == game_data[i + 6]) or \
                (game_data[0] == game_data[4] == game_data[8]) or \
                (game_data[2] == game_data[4] == game_data[6]):
            game_data[9] = player
            field_paint(game_data)
            print('Поздравляю, победили ' + player + ' ' + chr(127942))
            exit(print("Конец игры"))

        elif game_data[10] >= 9:
            game_data[9] = 0
            field_paint(game_data)
            print("\n")
            print('Ничья, победила дружба!' + chr(127881) + chr(127881))
            exit(print("Конец игры"))
    return game_data


def game(game_data):
    player = chr(10060)
    while game_data[9] != 0 and game_data[9] != chr(10060) and game_data[9] != chr(11093):
        field_paint(game_data)
        game_data = enter(game_data, player)
        check(game_data, player)
        print(game_data[10])

        game_data[10] += 1
        if player == chr(10060):
            player = chr(11093)
        elif player == chr(11093):
            player = chr(10060)


game_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 0]
game(game_data)
