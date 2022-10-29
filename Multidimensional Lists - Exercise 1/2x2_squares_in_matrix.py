def squares_containing_indentical_chars(matrix):
    count = 0

    for i in range(len(matrix) - 1):
        for x in range(len(matrix[i]) - 1):
            ll = []
            ll.append([matrix[i][x], matrix[i][x + 1], matrix[i + 1][x], matrix[i + 1][x + 1]])
            if ll[0].count(matrix[i][x]) == 4:
                count += 1

    return count


rows, cols = [int(x) for x in input().split()]
matrix = []

for i in range(rows):
    matrix.append([x for x in input().split()])

print(squares_containing_indentical_chars(matrix))