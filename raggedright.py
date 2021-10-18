from sys import stdin

lines = list(map(str.strip, stdin.readlines()))

lengths = list(map(len, lines))

n = max(lengths)
penalties = map(lambda m : (n - m) ** 2, lengths[:-1])

print(sum(penalties))
