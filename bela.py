n, b = input().split()

values = {'A': [11, 11],
          'K': [4,  4],
          'Q': [3,  3],
          'J': [20, 2],
          'T': [10, 10],
          '9': [14, 0],
          '8': [0,  0],
          '7': [0,  0]}


def getvalue(c):
    return values[c[0]][c[1] != b]


print(sum(getvalue(input()) for _ in range(int(n) * 4)))
