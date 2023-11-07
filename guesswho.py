import re

# parse
N, M, Q = map(int, input().split())

# get characters
characters = []

for _ in range(N):
    characters += [input()]

# create regex
r = list('.' * M)

for _ in range(Q):
    A, YN = input().split()
    r[int(A) - 1] = YN

r = re.compile(''.join(r))

# check for matches
matches = [bool(r.match(c)) for c in characters]

if sum(matches) == 1:
    print('unique')
    print(matches.index(True) + 1)

else:
    print('ambiguous')
    print(sum(matches))
