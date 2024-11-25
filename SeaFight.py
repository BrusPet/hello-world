from Class_SeaFight import Dot, Board, Ship
from random import randint
import time
import copy

print('Добро пожаловать в игру "Морской Бой"')
time.sleep(0.7)
answer = input('Желаете прочитать правила и обозначения игры? ')
if answer in ('da', 'Da', 'DA' 'ДА','Да', 'да', 'yes', 'Yes', 'YES'):
    print('Правила игры:'
          '1)Вы размещаете на своей доске корабли разной длинны.\n\n'
          '2)Размеры кораблей: 1 - 3х палубный, 2 - 2х палубных и 4 - однопалубных\n\n'
          '3)Размещать корабли можно только на доске на расстоянии в 1 клетку друг от друга\n\n'
          '1 - вертикальное направление(вниз), 0 - горизонтальное направление(вправо)\n\n'
          '4)Вы производите выстрелы по врагу поочередно с компьютером.\n\n'
          'В случае попадания, вы можете выстрелить ещё раз.\n\n'
          '5)Побеждает тот кто смог потопить все вражеские корабли\n')
    input('Нажмите "Enter", чтобы продолжить\n')
    print('Игровые обозначения:\n\n'
          '1-6 - координаты доски\n\n'
          ' O - неизвестная клетка\n\n'
          ''  ' - пустая клетка\n\n'
          ' T - промах(неудачи случаются)\n\n'
          ' S - палуба корабля\n\n'
          ' X - попадание по кораблю\n')
    input('Нажмите "Enter", чтобы продолжить\n')
print('Удачи в грядущем бою!')
time.sleep(0.7)
def print_boards(map1, map2):
    print('-------------------------------')
    print('Ваша доска              Доска соперника')
    for i in range(len(map1)):
        print(('| '.join(map1[i]) + '    ' + ('| '.join(map2[i]))))

board = [['  ', '1', '2', '3', '4', '5', '6'],
           ['1 ', 'O', 'O', 'O', 'O', 'O', 'O'],
           ['2 ', 'O', 'O', 'O', 'O', 'O', 'O'],
           ['3 ', 'O', 'O', 'O', 'O', 'O', 'O'],
           ['4 ', 'O', 'O', 'O', 'O', 'O', 'O'],
           ['5 ', 'O', 'O', 'O', 'O', 'O', 'O'],
           ['6 ', 'O', 'O', 'O', 'O', 'O', 'O']]
for i in board:
    print('| '.join(i))
user_board = copy.deepcopy(board)
ai_board = copy.deepcopy(board)
ships = [3, 2, 2, 1, 1, 1, 1]
user_ships = []
ai_ships = []
map1 = Board(user_board, len(ships), len(ships))
map2 = Board(copy.deepcopy(user_board), len(ships), len(ships))
ai_map1 = Board(ai_board, len(ships), len(ships))
ai_map2 = Board(copy.deepcopy(ai_board), len(ships), len(ships))
game_over = False
player = True

print('Для начала расставьте корабли на доске: ')
for i in range(7):
    flag = True
    while flag == True:
        ship = Dot(input('Введите x координату для ' + str(ships[i]) + ' палубного корабля '),
                input('Введите y координату для ' + str(ships[i]) + ' палубного корабля '))
        if ships[i] > 1:
            user_ship = Ship(ships[i], ship.get_dot(), direction=input('Введите направление корабля '))
            if user_ship.direction == '1':
                if ship.y > (7 - user_ship.long) or map1.board[ship.y][ship.x] != 'O' or map1.board[ship.y+1][ship.x] != 'O':
                    print('Неверные координаты расположения корабля!')
                    print("Попробуйте ещё раз!")
                    continue
            elif user_ship.direction == '0':
                if ship.x > (7 - user_ship.long) or map1.board[ship.y][ship.x] != 'O' or map1.board[ship.y][ship.x+1] != 'O':
                    print('Неверные координаты расположения корабля!')
                    print("Попробуйте ещё раз!")
                    continue
        elif ships[i] == 1:
            user_ship = Ship(ships[i], ship.get_dot())
            if map1.board[ship.y][ship.x] != 'O':
                print('Неверные координаты расположения корабля!')
                print("Попробуйте ещё раз!")
                continue
        map1.add_ship(map1.board, user_ship.dots())
        map1.contour(map1.board, user_ship.dots())
        for i in map1.board:
            print('| '.join(i))
        user_ships.append(user_ship.dots())
        flag = False
for i in map1.board:
    for j in i:
        if j == 'O':
            i[i.index(j)] = ' '

for i in range(7):
    flag = True
    while flag == True:
        ship = Dot(str(randint(1, 6)), str(randint(1, 6)))
        if ships[i] > 1:
            ai_ship = Ship(ships[i], ship.get_dot(), direction=str(randint(0,1)))
            if ai_ship.direction == '1':
                if ship.y > (7 - ai_ship.long) or ai_map1.board[ship.y][ship.x] != 'O' or ai_map1.board[ship.y + 1][ship.x] != 'O':
                    continue
            elif ai_ship.direction == '0':
                if ship.x > (7 - ai_ship.long) or ai_map1.board[ship.y][ship.x] != 'O' or ai_map1.board[ship.y][ship.x + 1] != 'O':
                    continue
        elif ships[i] == 1:
            ai_ship = Ship(ships[i], ship.get_dot())
            if ai_map1.board[ship.y][ship.x] != 'O':
                continue
        ai_map1.add_ship(ai_map1.board, ai_ship.dots())
        ai_map1.contour(ai_map1.board, ai_ship.dots())
        ai_ships.append(ai_ship.dots())
        flag = False
for i in ai_map1.board:
    for j in i:
        if j == 'O':
            i[i.index(j)] = ' '

print('Корабли расставлены!\n'
      'Приготовьтесь к бою!')
time.sleep(1.5)
user_hits = [[],[],[],[],[],[],[]]
ai_hits = [[],[],[],[],[],[],[]]
while game_over == False:
    print_boards(map1.board, map2.board)
    print('Начало нового раунда')
    time.sleep(1.5)
    if player:
        print('Ваша очередь стрельбы!')
        user_shot = Dot(input('Введите x координату для выстрела '),
                input('Введите y координату для выстрела '))
        shot = map2.shot(ai_map1.board, map2.board, user_shot.x, user_shot.y)
        time.sleep(1)
        if shot == 0:
            print('Вы ввели уже стрелянные координаты!')
            print('Попробуйте другие координаты!')
            continue
        if shot == 'T':
            print('Вы промахнулись! Очередь стрелять компьютера!')
            player = False
            continue
        if shot == 'X':
            print('Вы попали по вражескому кораблю!')
            time.sleep(1)
            map2.board[user_shot.y][user_shot.x] = 'X'
            turn = user_shot.get_dot()
            for i in range(len(ai_ships)):
                if turn in ai_ships[i]:
                    user_hits[i].insert(i, turn)
                    ai_ships[i].pop(ai_ships[i].index(turn))
                    if not ai_ships[i]:
                        print('Вы уничтожили вражеский корабль')
                        map2.contour(map2.board, user_hits[i])
                    else:
                        print('Вражеский корабль поврежден')
    if not player:
        print('Ход компьютера')
        time.sleep(1)
        ai_shot = Dot(str(randint(1,6)), str(randint(1,6)))
        shot = ai_map2.shot(map1.board, ai_map2.board, ai_shot.x, ai_shot.y)
        if shot == 0:
            continue
        print(f'Компьютер стреляет по координатам: ({ai_shot.x}, {ai_shot.y})')
        time.sleep(1)
        if shot == 'T':
            print('Компьютер промахнулся! Очередь стрелять игрока!')
            map1.board[ai_shot.y][ai_shot.x] = 'T'
            player = True
        if shot == 'X':
            map1.board[ai_shot.y][ai_shot.x] = 'X'
            print('Компьютер попал по вашему кораблю!')
            time.sleep(1)
            ai_map2.board[ai_shot.y][ai_shot.x] = 'X'
            turn = ai_shot.get_dot()
            for i in range(len(user_ships)):
                if turn in user_ships[i]:
                    ai_hits[i].insert(i, turn)
                    user_ships[i].pop(user_ships[i].index(turn))
                    if not user_ships[i]:
                        print('Компьютер уничтожил ваш корабль')
                        map2.contour(map2.board, user_hits[i])
                    else:
                        print('Ваш корабль поврежден')
            time.sleep(1)

    if user_ships == [[],[],[],[],[],[],[]] or ai_ships == [[],[],[],[],[],[],[]]:
        time.sleep(1)
        game_over = True
        if user_ships == [[],[],[],[],[],[],[]]:
            print('\n\nВсе ваши корабли были уничтожены!')
            print('\nВы Проиграли!')
        if ai_ships == [[],[],[],[],[],[],[]]:
            print('\n\nВсе корабли противника были уничтожены!')
            print('\nПоздравляем с Победой!')