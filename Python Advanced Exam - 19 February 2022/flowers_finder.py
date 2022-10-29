from collections import deque

vowels = deque(input().split())
consonants = input().split()
data = ['rose', 'tulip', 'lotus', 'daffodil']
flowers = data.copy()

letters = []


def check_words(vowel, consonant):
    for i in range(len(flowers)):
        if vowel in flowers[i]:
            flowers[i] = flowers[i].replace(vowel, "")
        if consonant in flowers[i]:
            flowers[i] = flowers[i].replace(consonant, '')

        if flowers[i] == '':
            return i


found_word = ''

while vowels and consonants:
    vowel = vowels.popleft()
    consonant = consonants.pop()

    result = check_words(vowel, consonant)

    if result is not None:
        found_word = data[result]
        break

if found_word:
    print(f"Word found: {found_word}")
else:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
