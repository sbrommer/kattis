from sys import stdin

n = int(stdin.readline())
answers = stdin.readline()[:-1]

guesses = ['ABC', 'BABC', 'CCAABB']
correct = [0, 0, 0]
names   = ['Adrian', 'Bruno', 'Goran']

for i in range(n):
    for j in range(3):
        guess = guesses[j]
        if answers[i] == guess[i % len(guess)]:
            correct[j] += 1

m = max(correct)

print(m)

for i in range(3):
    if correct[i] == m:
        print(names[i])
