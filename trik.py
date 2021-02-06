import sys
from functools import reduce

def swap(cup, move):
    if move == 'A':
        if cup == 1:
            return 2
        if cup == 2:
            return 1
        if cup == 3:
            return 3
    if move == 'B':
        if cup == 1:
            return 1
        if cup == 2:
            return 3
        if cup == 3:
            return 2

    if move == 'C':
        if cup == 1:
            return 3
        if cup == 2:
            return 2
        if cup == 3:
            return 1

moves = sys.stdin.readline()[:-1]

print(reduce(swap, moves, 1))

