def readints():
    return [int(i) for i in input().split()]


_, P, S = readints()

for _ in range(S):
    choice = set(readints()[1:])
    print('KEEP' if P in choice else 'REMOVE')
