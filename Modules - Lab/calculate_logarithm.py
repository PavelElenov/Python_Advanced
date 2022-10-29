from math import log


def logarithm(number, base):
    if base == 'natural':
        return f"{log(number):.2f}"
    else:
        return f'{log(number, int(base)):.2f}'
