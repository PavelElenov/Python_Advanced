from collections import deque

string = input().split()
data = deque()
operation = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a // b,
}

for el in string:
    if el not in "*+-/":
        data.append(int(el))
    else:
        separator = el

        while len(data) > 1:
            num_1 = data.popleft()
            num_2 = data.popleft()
            result = operation[separator](num_1, num_2)
            data.appendleft(result)

print(data[0])