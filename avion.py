from sys import stdin

found = False

for i in range(1, 6):
    blimp = stdin.readline()
    if 'FBI' in blimp:
        print(i, end=' ')
        found = True

if not found:
    print('HE GOT AWAY!')
