def rectangle(*args):
    def area():
        return length * width

    def perimeter():
        return 2 * (length + width)

    length, width = args
    result = {}
    if type(length) == int and type(width) == int:
        return f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"
    else:
        return 'Enter valid values!'


print(rectangle('2', 10))
