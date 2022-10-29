n = int(input())
matrix = []
row = 0
col = 0
for i in range(n):
    matrix.append([x for x in input().split()])

    if 'A' in matrix[i]:
        row = i
        col = matrix[i].index('A')

bags_of_tea = 0
make_it = True
matrix[row][col] = '*'

while True:
    command = input()

    if command:
        if command == 'up':
            row -= 1
        elif command == 'down':
            row += 1
        elif command == 'right':
            col += 1
        else:
            col -= 1

        if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix):
            make_it = False
        else:
            if matrix[row][col].isdigit():
                bags_of_tea += int(matrix[row][col])
            elif matrix[row][col] == 'R':
                make_it = False
            matrix[row][col] = '*'

        if not make_it or bags_of_tea >= 10:
            break
    else:
        break

if make_it:
    print('She did it! She went to the party.')
else:
    print("Alice didn't make it to the tea party.")

for el in matrix:
    print(' '.join(str(x) for x in el))


