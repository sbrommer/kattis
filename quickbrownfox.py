from sys import stdin

n = int(stdin.readline())

alphabet = set('abcdefghijklmnopqrstuvwxyz')

for _ in range(n):
    phrase = stdin.readline()
    phrase = set(map(lambda c: c.lower(), phrase))
    missing = alphabet - phrase

    if len(missing) == 0:
        print('pangram')
    else:
        missing =  list(missing)
        missing.sort()
        print('missing', ''.join(missing))
