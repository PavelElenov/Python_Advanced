stack = [int(i) for i in input().split()]
capacity = int(input())
count = 1
rack = capacity

while stack:
    cloth = stack[-1]

    if cloth <= rack:
        stack.pop()
        rack -= cloth
    else:
        count += 1
        rack = capacity

print(count)
