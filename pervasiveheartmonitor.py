from statistics import mean

o = open(0)


def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


line = o.readline().split()

while line:
    name = filter(lambda s: not is_float(s), line)
    hr = map(float, filter(is_float, line))

    print(mean(hr), end=' ')
    print(' '.join(name))

    line = o.readline().split()
