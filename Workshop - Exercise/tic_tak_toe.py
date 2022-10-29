from math import ceil


def choose_sign(player_one, player_two):
    def numeration_of_the_board():
        print('This is the numeration of the board:')
        return f"| 1 | 2 | 3 |\n| 4 | 5 | 6 |\n| 7 | 8 | 9 |"

    sign = input(f'{player_one} would you like to play with "X" or "O"? ')
    print(numeration_of_the_board())
    data = {}
    first_player = ''
    second_player = ''
    if sign == 'X':
        data[player_one] = 'X'
        data[player_two] = 'O'
        first_player = player_one
        second_player = player_two
    else:
        data[player_one] = 'O'
        data[player_two] = 'X'
        first_player = player_two
        second_player = player_one
    print(f"{first_player} starts first!")
    return data, first_player, second_player


def apply_sign(first_player, board, player_signs):
    def choose_position(first_player):
        position = int(input(f"{first_player} choose a free position [1-9]: "))
        row = ceil(position / 3) - 1
        col = position % 3 - 1
        if 9 < position < 1 :
            print("Position must be in range [1-9]!!!")
            return choose_position(first_player)
        if board[row][col] != " ":
            print('Please choose a free position!!!')
            return choose_position(first_player)
        return row, col

    row, col = choose_position(first_player)
    board[row][col] = player_signs[first_player]


def is_win(first_player, board, player_signs):
    first_player_sign = player_signs[first_player]
    diagonal1 = [board[0][0], board[1][1], board[2][2]]
    diagonal12 = [board[2][0], board[1][1], board[0][2]]
    for i in range(len(board)):
        row = board[i]
        column = [board[0][i], board[1][i], board[2][i]]
        if row.count(first_player_sign) == 3 or column.count(first_player_sign) == 3 or \
                diagonal1.count(first_player_sign) == 3 or diagonal12.count(first_player_sign) == 3:
            return True
    return False


def draw(board):
    for row in board:
        if " " in row:
            return False
    return True


def play(player_one, player_two, board):
    players_signs, first_player, second_player = choose_sign(player_one, player_two)
    win = False
    while True:
        apply_sign(first_player, board, players_signs)
        if is_win(first_player, board, players_signs):
            win = True
            break
        if draw(board):
            break
        print_board(board)
        first_player, second_player = second_player, first_player
    print_board(board)
    if win:
        print(f'{first_player} won!')
    else:
        print('DRAW!!!')


def build_board():
    board = []
    for _ in range(3):
        board.append([" "] * 3)
    return board


def print_board(board):
    for row in board:
        print('| ', end="")
        print(' | '.join([str(x) for x in row]), end='')
        print(' |')


board = build_board()
player_one = input('Player one name: ')
player_two = input("Player two name: ")
play(player_one, player_two, board)

