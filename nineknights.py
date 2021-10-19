from sys import stdin

def reachables(i, j):
    return set([(i-2, j-1), (i-2, j+1),
                (i-1, j-2), (i-1, j+2),
                (i+1, j-2), (i+1, j+2),
                (i+2, j-1), (i+2, j+1)])

def isvalid(knights):
    for knight in knights:
        if reachables(*knight).intersection(knights):
            return False
    return True

lines = stdin.readlines()

knights = set()
for i in range(5):
    for j in range(5):
        if lines[i][j] == 'k':
            knights.add((i, j))

print('valid' if len(knights) == 9 and isvalid(knights) else 'invalid')
