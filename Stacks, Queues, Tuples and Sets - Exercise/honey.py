from collections import deque

working_bees = deque([int(i) for i in input().split()])
nectars = [int(i) for i in input().split()]
symbols = deque(input().split())
honey = 0
operation = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: abs(x - y),
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
}

while working_bees and nectars:
    bee = working_bees.popleft()
    nectar = nectars.pop()

    if nectar >= bee:
        if nectar != 0:
            symbol = symbols.popleft()
            honey += operation[symbol](bee, nectar)
    else:
        working_bees.appendleft(bee)

print(f'Total honey made: {honey}')
if working_bees:
    print(f"Bees left: {', '.join(str(i) for i in working_bees)}")
if nectars:
    print(f'Nectar left: {", ".join(str(i) for i in nectars)}')




