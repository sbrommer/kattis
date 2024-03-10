from itertools import accumulate


def unscramble(b):
    b = bin(b)[2:].rjust(8, '0')
    message = list(accumulate(b[::-1],
                   lambda shifted, bit: int(int(bit) ^ shifted),
                   initial=0))

    message = ''.join(map(str, message[:0:-1]))
    return int(message, 2)


input()

print(*[unscramble(int(b)) for b in input().split()])
