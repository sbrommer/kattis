from random import randrange, choice

letters = 'abcdefghijklmnopqrstuvwxyz'
vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'


def generate_name():
    l = randrange(1, 19)

    name = choice(letters) + choice(letters)

    for _ in range(l):
        if name[-2] in vowels and name[-1] in vowels:
            name += choice(consonants)

        elif name[-2] in consonants and name[-1] in consonants:
            name += choice(vowels)

        else:
            name += choice(letters)

    return name


N = int(input())

names = set()

while len(names) < N:
    names.add(generate_name())

print(*names, sep='\n')
