map = [1, 2, 3, 4, 5, 6, 7, 8, 9]
victory = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
def maps():
    print('')
    print(map[0], map[1], map[2])
    print(map[3], map[4], map[5])
    print(map[6], map[7], map[8])
    return ''
def winner():
    win = ''
    for i in victory:
        if map[i[0]] == 'X' and map[i[1]] == 'X' and map[i[2]] == 'X':
            win = '1'
        if map[i[0]] == '0' and map[i[1]] == '0' and map[i[2]] == '0':
            win = '2'
    return win
def turn_maps(turn, sign):
    ind = map.index(turn)
    map[ind] = sign
game_over = False
player = True
while game_over == False:
    print(maps())
    if player is True:
        turn = int(input('Игрок 1, ваш ход '))
        sign = 'X'
    else:
        turn = int(input('Игрок 2, ваш ход '))
        sign = '0'
    turn_maps(turn, sign)
    win = winner()
    if win != '':
        game_over = True
    else:
        game_over = False
    player = not player
maps()
print('Победил Игрок', win)