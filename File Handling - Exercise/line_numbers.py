def count(line):
    words = line.split()
    letters_count = 0
    punctuation_mark_count = 0
    for word in words:
        for letter in word:
            if letter.isalpha():
                letters_count += 1
            else:
                punctuation_mark_count += 1
    return letters_count, punctuation_mark_count


with open('./txt.files/text.txt') as file, open('./txt.files/output.txt', 'w') as file2:
    for i, line in enumerate(file):
        letters, punctuation_marks = count(line)
        file2.write(f"Line {i + 1}: {line.strip()} ({letters})({punctuation_marks})\n")

file = open('./txt.files/output.txt')
print(file.read())
file.close()
