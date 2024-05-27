from collections import Counter


def readints():
    return [int(n) for n in input().split()]


k, q = [int(n) for n in input().split()]

bs = [int(input().split()[1]) for _ in range(q)]
c = Counter(bs)

print(0 if len(c) < k else min(c.values()))
