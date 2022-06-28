w = input()

for v in 'aeiou':
    w = w.replace(v + 'p' + v, v)

print(w)
