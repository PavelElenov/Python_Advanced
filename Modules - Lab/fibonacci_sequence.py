def create_fibonacci_sequance(number):
    ll = [0, 1]
    num1, num2 = ll
    for i in range(number - 2):
        num = num1 + num2
        ll.append(num)
        num1, num2 = num2, num
    return ll


def locate(sequence, number):
    if number in sequence:
        return f'The number - {number} is at index {sequence.index(number)}'
    else:
        return f'The number {number} is not in the sequence'
