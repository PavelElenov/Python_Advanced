from collections import deque

rows = int(input())
matrix = []
commands = deque(x for x in input().split())
coal_count = 0
m_row = 0
m_col = 0

for i in range(rows):
    matrix.append([x for x in input().split()])
    coal_count += matrix[i].count('c')

    if 's' in matrix[i]:
        m_row = i
        m_col = matrix[i].index('s')

collected = False
game_over = False

while commands:
    step = commands.popleft()

    if step == 'up':
        if m_row - 1 >= 0:
            matrix[m_row][m_col] = '*'
            m_row -= 1
        else:
            continue
    elif step == 'right':
        if m_col + 1 < rows:
            matrix[m_row][m_col] = '*'
            m_col += 1
        else:
            continue
    elif step == 'down':
        if m_row + 1 < rows:
            matrix[m_row][m_col] = '*'
            m_row += 1
        else:
            continue
    else:
        if m_col - 1 >= 0:
            matrix[m_row][m_col] = "*"
            m_col -= 1
        else:
            continue

    if matrix[m_row][m_col] == 'c':
        coal_count -= 1
        matrix[m_row][m_col] = 's'
    elif matrix[m_row][m_col] == 'e':
        game_over = True
        break

    if coal_count == 0:
        collected = True
        break

if collected:
    print(f'You collected all coal! ({m_row}, {m_col})')
elif game_over:
    print(f"Game over! ({m_row}, {m_col})")
else:
    print(f"{coal_count} pieces of coal left. ({m_row}, {m_col})")








