field = [
    ["0", "x1", "x2", "x3"],
    ["y1", "", "", ""],
    ["y2", "", "", ""],
    ["y3", "", "", ""],
]
# Пустое поле для игры в крестики нолики
value_list = ['0', 'X']
messages_list = ['Ход ноликов', 'Ход крестиков']

def show_field():
    print("Игровое поле")
    for i in field:
        print(i)
    print()
# Функция выводящая игровое поле

def input_error():
    print('Ошибка ввода, попробуйте еще раз')

def show_message():
    global messages_list
    print(messages_list[0])
    messages_list = messages_list[::-1]

def set_coords():
    global value_list
    try:
        x = int(input("Введите координату x:    "))
        y = int(input("Введите координату y:    "))
        if  field[y][x]:
            input_error()
            set_coords()
        else:
            field[y][x] = value_list[0]
            value_list = value_list[::-1]
    except:
        input_error()
        set_coords()

def win_check():
    for i in field:
        if i[1] == i[2] == i[3] and i[1]:
            return True
    for i in range(1, 4):
        if field[1][i] == field[2][i] == field[3][i] and field[1][i]:
            return True
    if (
        (field[1][1] == field[2][2] == field[3][3] or
        field[1][3] == field[2][2] == field[3][1]) and
        field[2][2]):
        return True

def win():
    if win_check():
        show_field()
        print(f"Победа {value_list[1]}'ов!")
        return True

def tie_game():
    if '' not in sum(field,[]):
        show_field()
        print("Ничья")
        return True

def play():
    show_field()
    show_message()
    set_coords()
    if win() or tie_game():
        return
    play()

play()

