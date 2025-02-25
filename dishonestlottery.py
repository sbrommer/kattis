from collections import Counter

n = int(input())
drawings = [int(x) for _ in range(10*n) for x in input().split()]
counter = Counter(drawings)
suspicious_nrs = [k for k, v in counter.items() if v > 2*n]

if suspicious_nrs:
    print(*sorted(suspicious_nrs))
else:
    print(-1)
