def concatenate(*args, **kwargs):
    result = "".join(args)
    for el in kwargs:
        if el in result:
            result = result.replace(el, kwargs[el])

    return result


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))