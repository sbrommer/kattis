import sys

line = sys.stdin.readline()
(n, m) = list(map(int, line.split()))

counts = {}

for cn in range(1, n+1):
    for cm in range(1, m+1):
        count = cn+cm
        if count in counts:
            counts[count] += 1
        else:
            counts[count] = 0

most = max(counts.values())

outcomes = []
for outcome, count in counts.items():
    if count == most:
        outcomes.append(outcome)

outcomes.sort()

for outcome in outcomes:
    print(outcome)