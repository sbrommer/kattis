from sys import stdin

n = int(stdin.readline())
aa = list(map(int, stdin.readline().split()))

winner = None
for a in range(6, 0, -1):
    if aa.count(a) == 1:
        winner = aa.index(a)
        break

if winner == None:
    print('none')
else:
    print(winner+1)