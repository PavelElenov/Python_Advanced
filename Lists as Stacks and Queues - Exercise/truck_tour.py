from collections import deque

petrol_pumps = int(input())
queue = deque()

for _ in range(petrol_pumps):
    petrol_info = [int(i) for i in input().split()]
    queue.append(petrol_info)

for attempt in range(petrol_pumps):
    current_petrol = 0
    failed = False
    for petrol, kilometers in queue:
        current_petrol += petrol

        if kilometers > current_petrol:
            queue.rotate(-1)
            failed = True
            break
        else:
            current_petrol -= kilometers

    if not failed:
        print(attempt)
        break


