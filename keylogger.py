from sys import stdin
from collections import deque

d = {'clank'  : 'A',
     'bong'   : 'B',
     'click'  : 'C',
     'tap'    : 'D',
     'poing'  : 'E',
     'clonk'  : 'F',
     'clack'  : 'G',
     'ping'   : 'H',
     'tip'    : 'I',
     'cloing' : 'J',
     'tic'    : 'K',
     'cling'  : 'L',
     'bing'   : 'M',
     'pong'   : 'N',
     'clang'  : 'O',
     'pang'   : 'P',
     'clong'  : 'Q',
     'tac'    : 'R',
     'boing'  : 'S',
     'boink'  : 'T',
     'cloink' : 'U',
     'rattle' : 'V',
     'clock'  : 'W',
     'toc'    : 'X',
     'clink'  : 'Y',
     'tuc'    : 'Z',
     'whack'  : 'space',
     'bump'   : 'caps',
     'pop'    : 'delete',
     'dink'   : 'shift',
     'thumb'  : 'shift'}

N = int(stdin.readline())

text = deque()
caps = False

for _ in range(N):
    sound = stdin.readline().strip()
    key = d[sound]

    if key in ['caps', 'shift']:
        caps = not caps

    elif key == 'delete':
        if len(text):
            text.pop()

    elif key == 'space':
        text.append(' ')

    else:
        key = key.upper() if caps else key.lower()
        text.append(key)

print(''.join(text))

