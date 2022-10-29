import sys


def find_eggs_number(move, row, col, matrix):
    total_eggs = 0
    eggs_cordinations = []

    while True:
        if move == 'up':
            row -= 1
        elif move == 'down':
            row += 1
        elif move == 'left':
            col -= 1
        else:
            col += 1

        if len(matrix) <= row or row < 0 or len(matrix) <= col or col < 0 or matrix[row][col] == 'X':
            break
        else:
            total_eggs += int(matrix[row][col])
            eggs_cordinations.append([row, col])
    return total_eggs, eggs_cordinations


n = int(input())
matrix = []
row = 0
col = 0

for _ in range(n):
    matrix.append([x for x in input().split()])

    if 'B' in matrix[_]:
        row = _
        col = matrix[_].index('B')

moves = ['up', 'down', 'left', 'right']
direction = ""
max_eggs_number = -sys.maxsize
max_eggs = []

while moves:
    move = moves.pop()

    eggs_number, eggs = find_eggs_number(move, row, col, matrix)

    if eggs_number > max_eggs_number:
        max_eggs_number = eggs_number
        direction = move
        max_eggs = eggs.copy()

print(direction)
print('\n'.join(str(x) for x in max_eggs))
print(max_eggs_number)



