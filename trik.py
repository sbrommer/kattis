from functools import reduce


moves = {'A': [0, 2, 1, 3],
         'B': [0, 1, 3, 2],
         'C': [0, 3, 2, 1]}


def swap(cup, move):
    return moves[move][cup]


print(reduce(swap, input(), 1))
