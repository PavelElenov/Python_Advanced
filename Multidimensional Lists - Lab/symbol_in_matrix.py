n = int(input())
matrix = []

for _ in range(n):
    string = input()
    ll = []

    for el in string:
        ll.append(el)

    matrix.append(ll)

symbol = input()
occur = False
for i in range(len(matrix)):
    if symbol in matrix[i]:
        print(f"({i}, {matrix[i].index(symbol)})")
        occur = True
        break

if not occur:
    print(f"{symbol} does not occur in the matrix")
