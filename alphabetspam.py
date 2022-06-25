line = input()

n = len(line)
w = line.count('_')
l = sum(c.islower() for c in line)
h = sum(c.isupper() for c in line)

print(w / n)
print(l / n)
print(h / n)
print((n - (w + l + h)) / n)
