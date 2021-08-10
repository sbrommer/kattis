from sys import stdin

def readint():
    return int(stdin.readline())

T = readint()

for _ in range(T):
    n = readint()

    pack = [n]

    for card in range(n-1, 0, -1):
        pack.insert(0, card)

        for _ in range(card):
            pack.insert(0, pack[-1])
            del pack[-1]

    print(*pack)
