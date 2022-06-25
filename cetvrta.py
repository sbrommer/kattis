cs = [map(int, input().split()) for _ in range(3)]
xs, ys = list(zip(*cs))

for x in set(xs):
    if xs.count(x) == 1:
        print(x)

for y in set(ys):
    if ys.count(y) == 1:
        print(y)
