def build_matrix(n):
    mm = []

    for i in range(n):
        ll = input().split()
        if 'T' in ll:
            col = ll.index("T")

            if not first_tunel_coordinates:
                first_tunel_coordinates['row'] = i
                first_tunel_coordinates['col'] = col
            else:
                second_tunel_coordinates['row'] = i
                second_tunel_coordinates['col'] = col
        mm.append(ll)
    return mm


n = int(input())
racing_number = input()
first_tunel_coordinates = {}
second_tunel_coordinates = {}
matrix = build_matrix(n)
row, col = 0, 0
total_kilometers = 0


def moving_car(command, row, col):
    if command == "up":
        row -= 1
    elif command == 'down':
        row += 1
    elif command == 'right':
        col += 1
    else:
        col -= 1

    return row, col


def check_position(row, col):
    position = ''
    if matrix[row][col] == 'F':
        position = 'F'
    elif matrix[row][col] == 'T':
        position = 'T'
    else:
        position = '.'

    return position


while True:
    command = input()

    if command == 'End':
        print(f"Racing car {racing_number} DNF.")
        break

    row, col = moving_car(command, row, col)
    current_position = check_position(row, col)

    if current_position == 'T':
        if row == first_tunel_coordinates['row'] and col == first_tunel_coordinates['col']:
            row = second_tunel_coordinates['row']
            col = second_tunel_coordinates['col']
        else:
            row = first_tunel_coordinates['row']
            col = first_tunel_coordinates['col']
        matrix[first_tunel_coordinates['row']][first_tunel_coordinates['col']] = '.'
        matrix[second_tunel_coordinates['row']][second_tunel_coordinates['col']] = '.'
        total_kilometers += 30
    elif current_position == 'F':
        total_kilometers += 10
        matrix[row][col] = '.'
        print(f"Racing car {racing_number} finished the stage!")
        break
    else:
        total_kilometers += 10

matrix[row][col] = 'C'
print(f"Distance covered {total_kilometers} km.")


def print_matrix():
    for line in matrix:
        print(''.join(line))


print_matrix()