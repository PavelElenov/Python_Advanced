def build_field(row, col):
    return [[0] * col for _ in range(row)]


def print_field(field):
    for row in field:
        print(row)


def apply_player_move(field, player_move, free_spaces, first_player):
    row, col = 0, 0
    row = free_spaces[player_move]
    col = player_move
    field[row][col] = first_player
    free_spaces[col] -= 1
    return row, col


def is_win(field, row, col, first_player):
    def backward(row, col, r, c, counter, field):
        new_row = row
        new_col = col
        while True:
            new_row -= r
            new_col -= c
            if is_valid(new_row, new_col):
                if field[new_row][new_col] == first_player:
                    counter += 1
                else:
                    break
            else:
                break
            if counter == 4:
                break
        return counter

    def is_valid(row, col):
        return 0 <= row < len(field) and 0 <= col < len(field[0])

    directions = [
        (0, 1),
        (-1, 0),
        (-1, 1),
        (1, 1),
    ]
    win = False
    for r, c in directions:
        counter = 1
        new_row = row
        new_col = col
        while True:
            new_row += r
            new_col += c
            if is_valid(new_row, new_col):
                if field[new_row][new_col] == first_player:
                    counter += 1
                else:
                    counter = backward(row, col, r, c, counter, field)
                    if counter < 4:
                        break
            else:
                counter = backward(row, col, r, c, counter, field)
                if counter < 4:
                    break
            if counter == 4:
                win = True
                break
    return win


def choose_column(first_player):
    column = int(input(f"Player {first_player}, please choose a column: ")) - 1
    if column >= len(field[0]):
        print('Colum must be in range[1-7]')
        choose_column(first_player)
    return column


def play(field):
    first_player, second_player = 1, 2
    free_spaces = [5] * 7
    while True:
        player_move = choose_column(first_player)
        row, col = apply_player_move(field, player_move, free_spaces, first_player)
        if is_win(field, row, col, first_player):
            break
        else:
            first_player, second_player = second_player, first_player
        print_field(field)
        print()
    print_field(field)
    print(f'The winner is player {first_player}')


field = build_field(6, 7)
print_field(field)
print()
play(field)

