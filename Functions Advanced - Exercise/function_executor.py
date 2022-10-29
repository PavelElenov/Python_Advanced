def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


def func_executor(*args):
    results = []
    for i in range(len(args)):
        func_name, params = args[i]
        results.append(f"{func_name.__name__} - {func_name(*params)}")
    return '\n'.join(results)


print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
))
