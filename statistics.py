from sys import stdin


line = stdin.readline()
i = 1

while line != '':
    _, *X = list(map(int, line.split()))
    print('Case ' + str(i) + ':', end=' ')
    print(min(X), end=' ')
    print(max(X), end=' ')
    print(max(X) - min(X))

    line = stdin.readline()
    i += 1