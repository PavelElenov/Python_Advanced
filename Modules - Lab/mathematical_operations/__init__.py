def divide(first_number, seconed_number):
    return f'{first_number / seconed_number:.2f}'


def multiply(first_number, second_number):
    return f"{first_number * second_number:.2f}"


def substract(first_number, second_number):
    return first_number - second_number


def add(first_number, second_number):
    return first_number + second_number


def raises(first_number, second_number):
    return f'{first_number ** second_number:.2f}'


def operations(first_number, sign, second_number):
    result = 0
    if sign == '/':
        result = divide(first_number, second_number)
    elif sign == '*':
        result = multiply(first_number, second_number)
    elif sign == '-':
        result = substract(first_number, second_number)
    elif sign == '+':
        result = add(first_number, second_number)
    else:
        result = raises(first_number, second_number)
    return result
