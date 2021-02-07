from sys import stdin

for w in stdin.readline().split():
    for v in 'aeiou':
        w = w.replace(v + 'p' + v, v)
    print(w, end=' ')
