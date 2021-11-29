from sys import stdin
from collections import deque

keystrokes = stdin.readline().strip()

l = deque()
r = deque()

for k in keystrokes:
    if k == 'B':
        l.pop()

    elif k == 'L':
        r.append(l.pop())

    elif k == 'R':
        l.append(r.pop())

    else:
        l.append(k)

print(''.join(l) + ''.join(reversed(list(r))))
