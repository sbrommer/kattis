from sys import stdin

def readline():
    return stdin.readline().strip()

word = readline()
letters = set(word)

alphabet = readline()

guessed = set()
c = 0
win = False
for letter in alphabet:
    guessed.add(letter)
    if letters.issubset(guessed):
        win = True
    if letter not in letters:
        c += 1
    if c == 10:
        break

print('win' if win else 'lose')