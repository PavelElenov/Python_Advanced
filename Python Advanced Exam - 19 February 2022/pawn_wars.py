white_paw = {'row': 0, 'col': 0}
black_paw = {'row': 0, 'col': 0}


def build_board():
    board = []
    for i in range(8):
        ll = input().split()
        if 'w' in ll:
            white_paw['row'] = i
            white_paw['col'] = ll.index('w')
        elif 'b' in ll:
            black_paw['row'] = i
            black_paw['col'] = ll.index('b')
        board.append(ll)
    return board


def can_capture(row, col, paw):
    if paw == white_paw:
        if col == 0:
            if board[row - 1][col + 1] == 'b':
                return True
        elif col == len(board) - 1:
            if board[row - 1][col - 1] == 'b':
                return True
        else:
            if board[row - 1][col - 1] == 'b' or board[row - 1][col + 1] == 'b':
                return True
    else:
        if col == 0:
            if board[row + 1][col + 1] == 'w':
                return True
        elif col == len(board) - 1:
            if board[row + 1][col - 1] == 'w':
                return True
        else:
            if board[row + 1][col - 1] == 'w' or board[row + 1][col + 1] == 'w':
                return True


def have_capture(paw):
    if paw == white_paw:
        row = white_paw['row']
        col = white_paw['col']
        win = can_capture(row, col, paw)

        if win:
            coordinates = chr(97 + black_paw['col']) + f'{len(board) - black_paw["row"]}'
            return f"Game over! White win, capture on {coordinates}."
    else:
        row = black_paw['row']
        col = black_paw['col']
        win = can_capture(row, col, paw)

        if win:
            coordinates = chr(97 + white_paw['col']) + f'{len(board) - white_paw["row"]}'
            return f"Game over! Black win, capture on {coordinates}."
    return False


def move_forward(paw):
    if paw == white_paw:
        board[white_paw['row']][white_paw['col']] = '-'
        white_paw['row'] -= 1
        board[white_paw['row']][white_paw['col']] = 'w'

        if white_paw['row'] == 0:
            coordinates = chr(97 + white_paw['col']) + f'{len(board) - white_paw["row"]}'
            return f"Game over! White pawn is promoted to a queen at {coordinates}."
    else:
        board[black_paw['row']][black_paw['col']] = '-'
        black_paw['row'] += 1
        board[black_paw['row']][black_paw['col']] = 'b'

        if black_paw['row'] == len(board) - 1:
            coordinates = chr(97 + black_paw['col']) + f'{len(board) - black_paw["row"]}'
            return f"Game over! Black pawn is promoted to a queen at {coordinates}."


board = build_board()
first, second = white_paw, black_paw

while True:
    if black_paw['col'] - 1 == white_paw['col'] or black_paw['col'] + 1 == white_paw['col']:
        result = have_capture(first)
        if result:
            print(result)
            break

    result = move_forward(first)
    if result:
        print(result)
        break

    first, second = second, first
