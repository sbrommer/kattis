from sys import stdin

# Read input
n = int(stdin.readline())

intervals = []

for _ in range(n):
    s, f = list(map(int, stdin.readline().split()))
    intervals.append((s, f))

# Sort intervals
intervals.sort(key=lambda i : -i[0])
intervals.sort(key=lambda i : i[1])

# Count non-overlapping intervals
n = 0
f = 0
for i in intervals:
    if i[0] >= f:
        n += 1
        f = i[1]

print(n)
