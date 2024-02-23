from collections import Counter

lines = open(0).read().split()
names = filter(lambda word: not word.isdigit(), lines)
attendance = Counter(names)

for name, n in sorted(attendance.items(), key=lambda t: -t[1]):
    print(n - 1, name)
