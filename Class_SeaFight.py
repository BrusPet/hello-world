class Dot:
    def __init__(self, x, y):
        while x == '' or y == '' or x not in ('1','2','3','4','5','6') or y not in ('1','2','3','4','5','6'):
            print('Неверные координаты! Попробуйте ещё раз!')
            x, y = input('Введите x координату '), input('Введите y координату ')
        self.x = int(x)
        self.y = int(y)
    def get_dot(self):
        return int(self.x), int(self.y)
class Ship:
    def __init__(self, long, dot, direction='1'):
        while direction not in ('0','1'):
            print('Указано неверное направление!')
            direction = input('Введите новое направление ')
        self.long = long
        self.dot = dot
        self.dot_x = dot[0]
        self.dot_y = dot[1]
        self.direction = direction
    def dots(self):
        dots_list = []
        if int(self.direction) == 0:
            for i in range(self.long):
                dots_list.append((self.dot_x + i, self.dot_y))
        if int(self.direction) == 1:
            for i in range(self.long):
                dots_list.append((self.dot_x, self.dot_y + i))
        return dots_list
class Board:

    def __init__(self, board, ships, alive):
        self.ships = ships
        self.board = board
        self.alive = alive
    def add_ship(self, board, ship):
        for i in ship:
            ind_y, ind_x = i
            board[ind_x][ind_y] = 'S'
    def contour(self, board, ship):
        for i in ship:
            ind_y, ind_x = i
            try:
                if board[ind_x][ind_y - 1] == 'O':
                    board[ind_x][ind_y - 1] = ' '
                if board[ind_x - 1][ind_y] == 'O':
                    board[ind_x - 1][ind_y] = ' '
                if ind_y + 1 < 7:
                    if board[ind_x][ind_y + 1] == 'O':
                        board[ind_x][ind_y + 1] = ' '
                if ind_x + 1 < 7:
                    if board[ind_x + 1][ind_y] == 'O':
                        board[ind_x + 1][ind_y] = ' '
            except IndexError:
                continue

    def shot(self,enemy_board, my_board, x, y):
        if enemy_board[int(y)][int(x)] == ' ':
            my_board[int(y)][int(x)] = 'T'
            return 'T'
        if enemy_board[int(y)][int(x)] == 'S':
            my_board[int(y)][int(x)] = 'X'
            return 'X'
        if my_board[int(y)][int(x)] == ('X' or 'T'):
            return 0