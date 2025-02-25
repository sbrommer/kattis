def parseints():
    return [*map(int, input().split())]


def pair(r1, r2):
    for i, a in enumerate(r1):
        if a in r2[:i] + r2[i+1:]:
            return 'YES'
    return 'NO'


t = int(input())

for _ in range(t):
    print(pair(parseints(), parseints()))
