from operator import eq

n = int(input())
answers = input()

guesses = ['ABC', 'BABC', 'CCAABB']
scores = [0, 0, 0]
names = ['Adrian', 'Bruno', 'Goran']

for i in range(n):
    for j in range(3):
        scores[j] = sum(map(eq, answers, guesses[j] * 34))

m = max(scores)

print(m)

for i in range(3):
    if scores[i] == m:
        print(names[i])
