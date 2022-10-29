rows, cols = [int(x) for x in input().split()]
word = input()
idx = 0

for i in range(rows):
    string = [None] * cols

    if i % 2 == 0:
        for j in range(cols):
            string[j] = word[idx % len(word)]
            idx += 1
    else:
        for j in range(cols - 1, -1, -1):
            string[j] = word[idx % len(word)]
            idx += 1
    print(''.join(string))
