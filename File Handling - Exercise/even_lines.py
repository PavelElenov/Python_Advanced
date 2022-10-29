from os import linesep

with open('./txt.files/text.txt') as file:
    lines = file.readlines()
    for i, line in enumerate(lines):
        if i % 2 == 0:
            result = ' '.join(line.strip().split()[::-1])
            for symbol in ["-", ",", ".", "!", "?"]:
                result = result.replace(symbol, '@')

            with open('./txt.files/output.txt', 'a') as file2:
                file2.write(result + '\n')
                file2.close()
        else:
            continue
    file.close()


with open('./txt.files/output.txt') as file:
    print(file.read())
    file.close()