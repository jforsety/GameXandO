# Задаем текст
text = """_____________________
Игра Крестики-нолики |
---------------------
"""

# Задаем вложенный список нашего поля
field = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


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
        if field[0][sign[0]] == field[0][sign[1]] == field[0][sign[2]]:
            return field[0][sign[0]]
        elif field[1][sign[0]] == field[1][sign[1]] == field[1][sign[2]]:
            return field[1][sign[0]]
        elif field[2][sign[0]] == field[2][sign[1]] == field[2][sign[2]]:
            return field[2][sign[0]]
    return False


# Функция игрового поля
def game_field(field):
    print(f"--------------\n"
          f"| {field[0][0]} | {field[0][1]} | {field[0][2]} |\n"
          f"| {field[1][0]} | {field[1][1]} | {field[1][2]} |\n"
          f"| {field[2][0]} | {field[2][1]} | {field[2][2]} |\n"
          f"--------------\n")


# Функция ввода значения, проверка корректности значений.
def check(token):
    value = False
    count = range(1, 10)
    while not value:
        player_input = int(input("Куда будем ставить " + token + "?: "))
        if player_input not in count:
            print("Вы ввели неверные координаты")
        elif 1 <= player_input <= 3:
            if str(field[0][player_input - 1]) not in "XO":
                field[0][player_input - 1] = token
                value = True
            else:
                print("Эта клетка уже занята!\n")
        elif 4 <= player_input <= 6:
            if str(field[1][player_input - 4]) not in "XO":
                field[1][player_input - 4] = token
                value = True
            else:
                print("Эта клетка уже занята!\n")
        elif 7 <= player_input <= 9:
            if str(field[2][player_input - 7]) not in "XO":
                field[2][player_input - 7] = token
                value = True
            else:
                print("Эта клетка уже занята!\n")
        else:
            print("Некорректный ввод. Введите число от 1 до 9.\n")


# Функция основного цикла игры
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
                break
        elif counter == 9:
            print("Ничья!\n")
            break



# Выводим начальный текст, главную функцию, ввод для завершения игры, либо начала новой игры.
print(text)
main(field)
key = input("Нажмите любую клавишу для выхода!\nЕсли хотите начать заново, то введите слово 'начать': ")
if key == "начать":
    print(text)
    main(field)
