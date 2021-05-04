from sys import stdin
from statistics import mean

def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

line = stdin.readline().split()

while line:
    name = filter(lambda s : not is_float(s), line)
    hr = map(float, filter(is_float, line))

    print(mean(hr), end=' ')
    print(' '.join(name))

    line = stdin.readline().split()
