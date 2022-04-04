from sys import stdin

qs = set()

for i in range(8):
    line = stdin.readline().strip()
    for j in range(8):
        if line[j] == '*':
            qs.add((i, j))

files = set(map(lambda q: q[0], qs))
ranks = set(map(lambda q: q[1], qs))

if files != set(range(8)):
    print('invalid')
elif ranks != set(range(8)):
    print('invalid')
else:
    invalid = False
    for q1 in qs:
        for q2 in qs:
            if q1 != q2 and abs(q1[0] - q2[0]) == abs(q1[1] - q2[1]):
                invalid = True
    print('invalid' if invalid else 'valid')
