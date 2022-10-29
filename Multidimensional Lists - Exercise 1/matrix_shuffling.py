def create_matrix():
    rows, cols = [int(x) for x in input().split()]
    mm = []

    for i in range(rows):
        mm.append([x for x in input().split()])

    return mm


def shuffling(matrix):
    while True:
        command = input()

        if command == 'END':
            break

        command = command.split()
        valid = True

        if command[0] == 'swap' and len(command) == 5:
            row1, col1, row2, col2 = int(command[1]), int(command[2]), int(command[3]), int(command[4])

            if row1 < len(matrix) and row2 < len(matrix) and col1 < len(matrix[0]) and col2 < len(matrix[0]):
                matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
            else:
                valid = False
        else:
            valid = False

        if valid:
            for el in matrix:
                print(' '.join(el))
        else:
            print('Invalid input!')


matrix = create_matrix()
shuffling(matrix)
