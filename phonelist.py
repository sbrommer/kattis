from sys import stdin

t = int(stdin.readline())

for _ in range(t):
    n = int(stdin.readline())
    ps = []
    for _ in range(n):
        ps.append(stdin.readline()[:-1])
    ps.sort()

    consistent = True
    for i in range(n-1):
        if ps[i] == ps[i+1][:len(ps[i])]:
            consistent = False

    print('YES' if consistent else 'NO')
