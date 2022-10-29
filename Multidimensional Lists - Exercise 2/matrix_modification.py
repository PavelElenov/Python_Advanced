rows = int(input())
matrix = []

for i in range(rows):
    matrix.append([int(x) for x in input().split()])

while True:
    command = input()

    if command == 'END':
        break

    command = command.split()
    row, col, value = int(command[1]), int(command[2]), int(command[3])
    invalid = False

    if command[0] == 'Add':
        if 0 <= row < rows and 0 <= col < rows:
            matrix[row][col] += value
        else:
            invalid = True
    else:
        if 0 <= row < rows and 0 <= col < rows:
            matrix[row][col] -= value
        else:
            invalid = True

    if invalid:
        print('Invalid coordinates')

for el in matrix:
    print(' '.join(str(x) for x in el))
