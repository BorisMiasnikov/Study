map = list(range(1,10))
win_comb = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(7,5,3),(1,5,9)]

def print_map():
    print('-------------')
    for i in range(3):
        print('|', map[0+i*3],'|', map[1+i*3],'|', map[2+i*3],'|')
        print('-------------')

def player_input(simvol):
    while True:
        value = input('В соотвтствии с нумерацией поля, укажите куда постаивть ' + simvol + ' ? ')
        if not (value in '123456789'):
            print('Не корректный ввод. Введите цифру от 1 до 9')
            continue
        value = int(value)
        if str(map[value - 1]) in 'XO':
            print('Эта клетк уже занята')
            continue
        map[value-1] = simvol
        break

def winner():
    for comb in win_comb:
        if map[comb[0]-1] == map[comb[1]-1] == map[comb[2]-1]:
            return map[comb[1]-1]


def game():
    counter = 0
    while True:
        print_map()
        if counter % 2 == 0:
            player_input('X')
        else:
            player_input('O')
        if counter > 3:
            win = winner()
            if win:
                print_map()
                print(win, 'победил')
                break
        counter += 1
        if counter > 8:
            print_map()
            print('Ничья')
            break

game()


