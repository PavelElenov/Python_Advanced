from os import remove
try:
    file = './txt.files/file_for_delete.txt'
    remove(file)
except FileNotFoundError:
    print('File already deleted!')