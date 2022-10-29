# print(' '.join(reversed(input().split())))
list = input().split()
stack = []

for i in range(len(list) - 1, -1, -1):
    stack.append(list.pop(i))

print(' '.join(stack))