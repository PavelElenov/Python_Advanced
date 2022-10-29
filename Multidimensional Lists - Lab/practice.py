matrix = []
n = 5
m = 7

for _ in range(n):
    list = []
    for i in range(m):
        list.append(0)

    matrix.append(list)
print('\n'.join(str(i)for i in matrix))