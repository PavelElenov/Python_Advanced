from collections import deque

string = deque(input().split())
colors = ['red', 'yellow', 'blue', 'orange', 'purple', 'green']
collected_colors = []
special_colors = {
    'orange': ['red', 'yellow'],
    'purple': ['red', 'blue'],
    'green': ['yellow', 'blue'],
}

while string:
    left = string.popleft()
    right = string.pop() if string else ''

    result = left + right
    if result in colors:
        collected_colors.append(result)
        continue

    result = right + left
    if result in colors:
        collected_colors.append(result)
        continue

    left = left[:-1]
    right = right[:-1]
    if left:
        string.insert(len(string) // 2, left)
    if right:
        string.insert(len(string) // 2, right)

for color in collected_colors:
    if color in special_colors:
        for main_color in special_colors[color]:
            if main_color not in collected_colors:
                collected_colors.remove(color)
                break

print(collected_colors)


