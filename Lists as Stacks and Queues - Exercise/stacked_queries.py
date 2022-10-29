n = int(input())
stack = []

for i in range(n):
    queries = input()

    if queries[0] == '1':
        queries = queries.split()
        number = int(queries[1])
        stack.append(number)
    else:
        if len(stack) > 0:
            if queries == '2':
                stack.pop()
            elif queries == '3':
                print(max(stack))
            else:
                print(min(stack))

stack = stack[::-1]
print(', '.join(str(i) for i in stack))