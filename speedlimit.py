from operator import sub, mul

n = int(input())

while n >= 0:
    # parse
    inp = [map(int, input().split()) for _ in range(n)]
    ss, ts = map(list, zip(*inp))

    # calculate distance
    ts = map(sub, ts, [0] + ts)
    d = sum(map(mul, ss, ts))

    print(d, 'miles')

    n = int(input())
