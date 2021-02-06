from sys import stdin

t = int(stdin.readline())

for _ in range(t):
    s1 = stdin.readline()[:-1]
    s2 = stdin.readline()[:-1]

    print(s1)
    print(s2)

    for i in range(len(s1)):
        print('.' if s1[i] == s2[i] else '*', end='')

    print('\n')