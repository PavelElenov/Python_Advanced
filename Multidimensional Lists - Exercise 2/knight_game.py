def find_count(row, col, matrix):
    moves = [
        [row + 1, col - 2],
        [row + 1, col + 2],
        [row - 1, col - 2],
        [row - 1, col + 2],
        [row + 2, col - 1],
        [row + 2, col + 1],
        [row - 2, col - 1],
        [row - 2, col + 1],
    ]

    count = 0

    for r, c in moves:
        if 0 <= r < len(matrix) and 0 <= c < len(matrix) and matrix[r][c] == 'K':
            count += 1
    return count


rows = int(input())
matrix = []

for _ in range(rows):
    matrix.append([x for x in input()])

max_count = 0
max_k_row = 0
max_k_col = 0
removes = 0

while True:
    for row in range(rows):
        for col in range(rows):
            if matrix[row][col] == 'K':
                count = find_count(row, col, matrix)

                if count > max_count:
                    max_count = count
                    max_k_row = row
                    max_k_col = col

    if max_count > 0:
        matrix[max_k_row][max_k_col] = '0'
        removes += 1
        max_count = 0
    else:
        break

print(removes)