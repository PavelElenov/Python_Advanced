try:
    file = open('./txt.files/text.txt')
    print('File found')
except FileNotFoundError:
    print('File not found')



