from collections import deque


def fill_the_box(*args):
    height, length, width = args[:3]
    args = deque(args[3:])
    size_of_the_box = height * length * width
    free_space = True

    while True:
        element = args.popleft()
        if element != "Finish":
            if size_of_the_box > 0:
                if size_of_the_box - element >= 0:
                    size_of_the_box -= element
                else:
                    element -= size_of_the_box
                    size_of_the_box = 0
                    args.appendleft(element)
                    free_space = False
            else:
                args.appendleft(element)
                free_space = False
        else:
            break

        if not free_space:
            if args:
                args.remove("Finish")
                break
    if free_space:
        return f"There is free space in the box. You could put {size_of_the_box} more cubes."
    else:
        return f"No more free space! You have {sum(args)} more cubes."


print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
