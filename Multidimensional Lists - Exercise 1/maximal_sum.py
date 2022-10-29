import sys
rows, cols = [int(x) for x in input().split()]
matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

max_sum = -sys.maxsize
square = []

for i in range(rows - 2):
    for j in range(cols - 2):
        ll = []
        ll.append([[matrix[i][j], matrix[i][j + 1], matrix[i][j + 2]],
                   [matrix[i + 1][j], matrix[i + 1][j + 1], matrix[i + 1][j + 2]],
                   [matrix[i + 2][j], matrix[i + 2][j + 1], matrix[i + 2][j + 2]]])
        current_sum = sum(ll[0][0]) + sum(ll[0][1]) + sum(ll[0][2])

        if current_sum > max_sum:
            max_sum = current_sum
            square = ll.copy()

print(f"Sum = {max_sum}")

for el in square[0]:
    print(' '.join(str(x) for x in el))

