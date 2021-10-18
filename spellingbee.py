from sys import stdin

bee = stdin.readline().strip()

c = bee[0]
bee = set(bee)

n = int(stdin.readline().strip())

for _ in range(n):
    word = stdin.readline().strip()
    if len(word) >= 4 and c in word and set(word).issubset(bee):
        print(word)
