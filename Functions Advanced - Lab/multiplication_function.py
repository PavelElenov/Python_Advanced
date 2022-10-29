def multiply(*args):
    mult = 1

    for value in args:
        mult *= value
    return mult


print(multiply(1, 4, 5))