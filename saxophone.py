from operator import sub
from itertools import starmap

fingers = {
    'c': [0, 1, 1, 1, 0, 0, 1, 1, 1, 1],
    'd': [0, 1, 1, 1, 0, 0, 1, 1, 1, 0],
    'e': [0, 1, 1, 1, 0, 0, 1, 1, 0, 0],
    'f': [0, 1, 1, 1, 0, 0, 1, 0, 0, 0],
    'g': [0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    'a': [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    'b': [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    'C': [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    'D': [1, 1, 1, 1, 0, 0, 1, 1, 1, 0],
    'E': [1, 1, 1, 1, 0, 0, 1, 1, 0, 0],
    'F': [1, 1, 1, 1, 0, 0, 1, 0, 0, 0],
    'G': [1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    'A': [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    'B': [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
}

t = int(input())

for _ in range(t):
    song = input()

    total = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    previous = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for note in song:
        next = fingers[note]
        total = [t + (n and not p) for t, p, n in zip(total, previous, next)]
        previous = next

    print(*total)
