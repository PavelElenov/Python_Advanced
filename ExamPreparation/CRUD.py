def create_matrix():
    mm = []
    for i in range(6):
        ll = input().split()
        mm.append(ll)
    return mm


def create(matrix, direction , value, row, col):
    if direction == 'up':
        if matrix[row - 1][col] == '.':
            matrix[row - 1][col] = value
        row -= 1
    elif direction == 'down':
        if matrix[row + 1][col] == '.':
            matrix[row + 1][col] = value
        row += 1
    elif direction == 'left':
        if matrix[row][col - 1] == '.':
            matrix[row][col - 1] = value
        col -= 1
    elif direction == 'right':
        if matrix[row][col + 1] == '.':
            matrix[row][col + 1] = value
        col += 1
    return row, col


def update(matrix, direction , value, row, col):
    if direction == 'up':
        if matrix[row - 1][col] != '.':
            matrix[row - 1][col] = value
        row -= 1
    elif direction == 'down':
        if matrix[row + 1][col] != '.':
            matrix[row + 1][col] = value
        row += 1
    elif direction == 'left':
        if matrix[row][col - 1] != '.':
            matrix[row][col - 1] = value
        col -= 1
    elif direction == 'right':
        if matrix[row][col + 1] != '.':
            matrix[row][col + 1] = value
        col += 1
    return row, col


def delete(matrix, direction, row, col):
    if direction == 'up':
        if matrix[row - 1][col] != '.':
            matrix[row - 1][col] = '.'
        row -= 1
    elif direction == 'down':
        if matrix[row + 1][col] != '.':
            matrix[row + 1][col] = '.'
        row += 1
    elif direction == 'left':
        if matrix[row][col - 1] != '.':
            matrix[row][col - 1] = '.'
        col -= 1
    elif direction == 'right':
        if matrix[row][col + 1] != '.':
            matrix[row][col + 1] = '.'
        col += 1
    return row, col


def read(matrix, direction, row, col):
    if direction == 'up':
        if matrix[row - 1][col] != '.':
            print(matrix[row - 1][col])
        row -= 1
    elif direction == 'down':
        if matrix[row + 1][col] != '.':
            print(matrix[row + 1][col])
        row += 1
    elif direction == 'left':
        if matrix[row][col - 1] != '.':
            print(matrix[row][col - 1])
        col -= 1
    elif direction == 'right':
        if matrix[row][col + 1] != '.':
            print(matrix[row][col + 1])
        col += 1
    return row, col


def print_matrix():
    for row in matrix:
        print(' '.join(row))


matrix = create_matrix()
start_position = [int(x) for x in input().replace('(', '').replace(')', '').split(', ')]
row, col = start_position

while True:
    command = input()

    if command == 'Stop':
        break

    command = command.split(', ')

    if command[0] == 'Create':
        direction, value = command[1], command[2]
        row, col = create(matrix, direction, value, row, col)
    elif command[0] == 'Update':
        direction, value = command[1], command[2]
        row, col = update(matrix, direction, value, row, col)
    elif command[0] == 'Delete':
        direction = command[1]
        row, col = delete(matrix, direction, row, col)
    else:
        direction = command[1]
        row, col = read(matrix, direction, row, col)

print_matrix()
