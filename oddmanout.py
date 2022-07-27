def readints():
    return list(map(int, input().split()))


n, = readints()

for i in range(1, n + 1):
    print('Case #' + str(i) + ':')

    g, = readints()
    cs = readints()

    c_set = set()

    for c in cs:
        if c not in c_set:
            c_set.add(c)
        else:
            c_set.remove(c)

    print(list(c_set)[0])
