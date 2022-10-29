from collections import deque

seats = input().split(', ')
first_sequence = deque(int(x) for x in input().split(', '))
second_sequence = [int(x) for x in input().split(", ")]
seats_matches = []
rotation = 0


def check_for_matches(character):
    for seat in seats:
        for letter in seat:
            if letter.isalpha():
                if letter == character:
                    seats.remove(seat)
                    return seat

    #Check for character in seats_matches
    for seat in seats_matches:
        for letter in seat:
            if letter.isalpha():
                if letter == character:
                    return seat

    return False


while len(seats_matches) < 3 and rotation < 10:
    first_number = first_sequence.popleft()
    second_number = second_sequence.pop()

    character = chr(first_number + second_number)
    have_matches = check_for_matches(character)

    if have_matches:
        seat = have_matches

        if seat not in seats_matches:
            seats_matches.append(seat)
    else:
        first_sequence.append(first_number)
        second_sequence.insert(0, second_number)

    rotation += 1

print(f"Seat matches: {', '.join(seats_matches)}")
print(f"Rotations count: {rotation}")
