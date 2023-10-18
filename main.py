# Задаем текст
text = """_____________________
Игра Крестики-нолики |
---------------------
"""

# Задаем список поля
field = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# Функция победных комбинаций
def check_win(field):
    win = [[0, 1, 2],
           [3, 4, 5],
           [6, 7, 8],
           [0, 3, 6],
           [1, 4, 7],
           [2, 5, 8],
           [0, 4, 8],
           [2, 4, 6]]
    for sign in win:
        if field[sign[0]] == field[sign[1]] == field[sign[2]]:
            return field[sign[0]]
    return False


# Функция игрового поля
def game_field(field):
    print(f"--------------\n"
          f"| {field[0]} | {field[1]} | {field[2]} |\n"
          f"| {field[3]} | {field[4]} | {field[5]} |\n"
          f"| {field[6]} | {field[7]} | {field[8]} |\n"
          f"--------------\n")


# Функция ввода значения, проверка корректности значений.
def check(token):
    value = False
    count = range(1, 10)
    while not value:
        player_input = int(input("Куда будем ставить " + token + " ?: "))
        if player_input not in count:
            print("Вы ввели неверные координаты")
        elif 1 <= player_input <= 9:
            if str(field[player_input - 1]) not in "XO":
                field[player_input - 1] = token
                value = True
            else:
                print("Эта клетка уже занята!\n")
        else:
            print("Некорректный ввод. Введите число от 1 до 9.\n")


# Функция основного цикла игры
def next_game(field):
    def main(field):
        counter = 0
        win = False
        while not win:
            game_field(field)
            if counter % 2 == 0:
                check("X")
            else:
                check("O")
            counter += 1
            if counter > 4:
                result = check_win(field)
                if result:
                    print(f"Победитель {result} !!!\n")
                    game_field(field)
                    break
            elif counter == 9:
                print("Ничья!\n")
                game_field(field)
                break
    main(field)
    key = input("Нажмите любую клавишу для выхода!\nЕсли хотите начать заново, то введите слово 'начать': ")
    if key == "начать":
        print(text)
        field = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        main(field)

# Выводим начальный текст, главную функцию.
print(text)
next_game(field)