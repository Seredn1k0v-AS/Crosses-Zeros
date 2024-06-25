field = [
    ["0", "x1", "x2", "x3"],
    ["y1", ".", ".", "."],
    ["y2", ".", ".", "."],
    ["y3", ".", ".", "."],
]
# Пустое поле для игры в крестики нолики

def show_field():
    print()
    print("Игровое поле")
    print()
    for i in field:
        print(i)
    print()
# Функция выводящая игровое поле


def play_0():
    print("Ход ноликов")
    x = int(input("Введите координату x:    "))
    if x < 1 or x > 3:
        print("Ошибка, вы вышли за пределы игрового поля")
        play_0()
    y = int(input("Введите координату y:    "))
    if y < 1 or y > 3:
        print("Ошибка, вы вышли за пределы игрового поля")
        play_0()
    if field[y][x] == ".":
        field[y][x] = '0'
    else:
        print("Ошибка ввода. Выберете свободдное поле!")
        play_0()
    print()
    show_field()
    print()
    win()
    if stop:

        return "Конец игры"
    else:
        play_x()

def play_x():
    print("Ход крестиков")
    x = int(input("Введите координату x:    "))
    if x < 1 or x > 3:
        print("Ошибка, вы вышли за пределы игрового поля")
        play_x()
    y = int(input("Введите координату y:    "))
    if y < 1 or y > 3:
        print("Ошибка, вы вышли за пределы игрового поля")
        play_x()
    if field[y][x] == ".":
        field[y][x] = 'x'
    else:
        print("Ошибка ввода. Выберете свободдное поле!")
        play_x()
    show_field()
    win()
    if stop:
        print()
        return 'Конец игры'
    else:
        play_0()

def win():
    global stop
    stop = False
    for i in field:
            if (i[1] == i[2]) and (i[2] == i[3] and i[2] != "."):
                if i[1] == '0':
                    winner = 'Нолики'
                else:
                    winner = 'Крестики'
                print(f'Победила команда {winner}')

                stop = True
                return
#   Проверяем победные комбинации по горизонтали
    for i in range(1,4):
        if (field[1][i] == field[2][i] and
            field[2][i] == field[3][i] and
            field[2][i] != "."
        ):
            if field[1][i] == '0':
                winner = 'Нолики'
            else:
                winner = 'Крестики'
            print(f'Победила команда {winner}')

            stop = True
            return
#   Проверяем победные комбинации по вертикали

    if ((field[1][1] == field[2][2] and
        field[2][2] == field[3][3]
        or
        field[1][3] == field[2][2] and
        field[2][2] == field[3][1])

        and field[2][2] != "."
    ):
        if field[2][2] == '0':
            winner = 'Нолики'
        else:
            winner = 'Крестики'
        print(f'Победила команда {winner}')

        stop = True
        return


    if '.' not in sum(field,[]):
        print("Ничья")
        stop = True
# Проверака на заполненность поля без победных комбинаций1

print(sum(field,[]))
show_field()
play_0()