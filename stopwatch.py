import sys

def readint():
    return int(sys.stdin.readline())

n = readint()

if n % 2 == 1:
    print('still running')

else:
    s = 0

    for _ in range(int(n / 2)):
        on  = readint()
        off = readint()
        s += off - on

    print(s)
