n = int(input())
matrix = []

for i in range(n):
    matrix.append([int(x) for x in input().split()])

primary_diagonal = [matrix[i][i] for i in range(len(matrix))]
secondary_diagonal = [matrix[i][len(matrix) - 1 - i] for i in range(len(matrix))]

print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))
