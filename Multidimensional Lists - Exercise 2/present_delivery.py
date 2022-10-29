presents = int(input())
size = int(input())
matrix = []
nice_kids_count = 0
santa_row = 0
santa_col = 0

for i in range(size):
    matrix.append([x for x in input().split()])

    if 'S' in matrix[i]:
        santa_row = i
        santa_col = matrix[i].index('S')

    if 'V' in matrix[i]:
        nice_kids_count += matrix[i].count('V')


def directions(direction, santa_row, santa_col):
    if direction == 'up':
        santa_row -= 1
    elif direction == 'down':
        santa_row += 1
    elif direction == 'left':
        santa_col -= 1
    else:
        santa_col += 1
    return santa_row, santa_col


def is_valid(row, col, size):
    return 0 <= row < size and 0 <= col < size


def check_position(row, col):
    if matrix[row][col] == 'V':
        return 'V'
    elif matrix[row][col] == 'C':
        return 'C'
    else:
        return '-'


def c_position(row, col):
    positions = [
        [row - 1, col],
        [row + 1, col],
        [row, col + 1],
        [row, col -1]
    ]
    kids = ['V', 'X']
    gives = 0
    n_kids = 0

    for r, c in positions:
        if is_valid(r, c, size):
            if matrix[r][c] in kids:
                gives += 1
                if matrix[r][c] == 'V':
                    n_kids += 1
                matrix[r][c] = '-'
    return gives, n_kids


run_out = False
manages_all = False
nice_kids = nice_kids_count

while True:
    command = input()

    if command == "Christmas morning":
        break

    direction = command
    row, col = directions(direction, santa_row, santa_col)

    if is_valid(row, col, size):
        matrix[santa_row][santa_col] = '-'
        position = check_position(row,  col)

        if position == 'V':
            nice_kids -= 1
            presents -= 1
        elif position == 'C':
            gived_presents, kids = c_position(row, col)
            presents -= gived_presents
            nice_kids -= kids

        matrix[row][col] = "S"
        santa_row, santa_col = row, col

        if nice_kids <= 0:
            manages_all = True
            break

        if presents <= 0:
            run_out = True
            break


if run_out:
    print('Santa ran out of presents!')

for el in matrix:
    print(' '.join(el))

if manages_all:
    print(f"Good job, Santa! {nice_kids_count} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids} nice kid/s.")




