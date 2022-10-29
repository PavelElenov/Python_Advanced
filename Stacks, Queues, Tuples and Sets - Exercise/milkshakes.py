from collections import deque

chocolates = list(int(i) for i in input().split(', '))
cups_of_milk = deque(int(i) for i in input().split(', '))

milkshakes = 0

while chocolates and cups_of_milk and milkshakes < 5:
    chocolate = chocolates.pop()
    milk = cups_of_milk.popleft()

    if milk <= 0 and chocolate <= 0:
        continue
    if milk <= 0:
        chocolates.append(chocolate)
        continue
    if chocolate <= 0:
        cups_of_milk.appendleft(milk)
        continue

    if chocolate != milk:
        chocolates.append(chocolate - 5)
        cups_of_milk.append(milk)
    else:
        milkshakes += 1


if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print('Not enough milkshakes.')

if chocolates:
    print(f"Chocolate: {', '.join(str(el) for el in chocolates)}")
else:
    print("Chocolate: empty")

if cups_of_milk:
    print(f"Milk: {', '.join(str(el) for el in cups_of_milk)}")
else:
    print("Milk: empty")



