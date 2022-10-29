def operate(param, *args):
    def summation():
        return sum(args)

    def substract():
        result = args[0]
        for v in args[1:]:
            result -= v
        return result

    def multiplication():
        result = 1
        for v in args:
            result *= v
        return result

    def division():
        result = args[0]
        for v in args[1:]:
            if v != 0:
                result /= v
        return result

    if param == '+':
        return summation()
    elif param == '-':
        return substract()
    elif param == '*':
        return multiplication()
    else:
        return division()


print(operate("-", 10, 2))
