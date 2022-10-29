def exit_founder(*args):
    first_player, second_player = args
    matrix = []
    for i in range(6):
        matrix.append([x for x in input().split()])
    rest = {'Tom': False, "Jerry": False}
    while True:
        coordinates = input()

        if rest[first_player]:
            rest[first_player] = False
            first_player, second_player = second_player, first_player
            continue

        for el in coordinates:
            if el in ['(', ')']:
                coordinates = coordinates.replace(el, '')
        row, col = [int(x) for x in coordinates.split(', ')]

        if matrix[row][col] == 'E':
            print(f"{first_player} found the Exit and wins the game!")
            return
        elif matrix[row][col] == 'T':
            print(f"{first_player} is out of the game! The winner is {second_player}.")
            return
        elif matrix[row][col] == 'W':
            print(f"{first_player} hits a wall and needs to rest.")
            rest[first_player] = True

        first_player, second_player = second_player, first_player


# first_player, second_player = input().split(', ')
# exit_founder(first_player, second_player)
