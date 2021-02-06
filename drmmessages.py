from sys import stdin

def rotate(m):
    v = sum(m)
    return list(map(lambda c : (c + v) % 26, m))

m = stdin.readline()[:-1]

m = list(map(lambda c : ord(c) - ord('A'), m))
l = len(m)//2

ml = rotate(m[:l])
mr = rotate(m[l:])

for i in range(l):
    ml[i] = (ml[i] + mr[i]) % 26

m = list(map(lambda c : chr(c + ord('A')), ml))

print(''.join(m))
