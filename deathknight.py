from sys import stdin

n = int(stdin.readline())
won = 0

for _ in range(n):
    battle = stdin.readline().strip()
    won += 'CD' not in battle

print(won)