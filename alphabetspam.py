import sys

line = sys.stdin.readline()[:-1]

n = len(line)
w = line.count('_')
l = len(list(filter(lambda c : c.islower(), line)))
h = len(list(filter(lambda c : c.isupper(), line)))

print(w / n)
print(l / n)
print(h / n)
print((n - (w + l + h)) / n)