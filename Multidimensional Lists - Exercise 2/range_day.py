def moving(matrix, my_row, my_col, direction, steps):
        row = my_row
        col = my_col
        if direction == 'up':
            row -= steps
        elif direction == 'down':
            row += steps
        elif direction == 'right':
            col += steps
        else:
            col -= steps

        if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix) or matrix[row][col] == 'x':
            return my_row, my_col
        else:
            matrix[my_row][my_col] = '.'
            return row, col


def shooting(direction, matrix, my_row, my_col, targets, targets_list):
    row = my_row
    col = my_col

    while True:
        if direction == 'up':
            row -= 1
        elif direction == 'down':
            row += 1
        elif direction == 'right':
            col += 1
        else:
            col -= 1
        if 0 <= row < len(matrix) and 0 <= col < len(matrix):
            if matrix[row][col] == 'x':
                matrix[row][col] = '.'
                targets_list.append([row, col])
                return targets - 1
            else:
                continue
        else:
            return targets


matrix = []
my_row = 0
my_col = 0
targets = 0
for i in range(5):
    matrix.append([x for x in input().split()])

    if 'A' in matrix[i]:
        my_row = i
        my_col = matrix[i].index('A')
    targets += matrix[i].count('x')

n = int(input())

targets_list = []

for _ in range(n):
    command = input().split()

    if command[0] == 'move':
        direction, steps = command[1], int(command[2])
        my_row, my_col = moving(matrix, my_row, my_col, direction, steps)
    else:
        direction = command[1]
        targets = shooting(direction, matrix, my_row, my_col, targets, targets_list)
        if targets == 0:
            break

if targets == 0:
    print(f"Training completed! All {len(targets_list)} targets hit.")
else:
    print(f"Training not completed! {targets} targets left.")

print(*targets_list, sep='\n')

