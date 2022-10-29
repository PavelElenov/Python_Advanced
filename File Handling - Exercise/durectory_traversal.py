from collections import defaultdict
from os import listdir
from os.path import isdir, join

directory_path = input()


def directory_traversal(path):
    for element in listdir(path):
        if isdir(join(path, element)):
            if element != "venv" and element != '.idea':
                directory_traversal(join(path, element))
        else:
            extension = element.split('.')[-1]
            data["." + extension].append(element)


data = defaultdict(list)

directory_traversal(directory_path)

for key, value in data.items():
    print(key)
    for el in value:
        print(f"- - - {el}")
