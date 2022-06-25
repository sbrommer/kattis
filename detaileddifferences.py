from operator import eq

n = int(input())

for _ in range(n):
    s1 = input()
    s2 = input()

    print(s1)
    print(s2)

    print(*['*.'[e] for e in map(eq, s1, s2)], sep='')

