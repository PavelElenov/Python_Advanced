from collections import deque

quantity = int(input())
queue = deque(int(i) for i in input().split())
complete = True
print(max(queue))

while True:
    if len(queue) == 0:
        break

    if queue[0] <= quantity:
        quantity -= queue[0]
        queue.popleft()
    else:
        complete = False
        break

if complete:
    print('Orders complete')
else:
    print(f"Orders left: {' '.join(str(i) for i in queue)}")