nab, *ws = open(0).readlines()

n, a, b = map(int, nab.split())
ws = list(map(int, ws))

if a in ws and b in ws:
    print(*range(a, b + 1))

elif a in ws:
    print(b)

elif b in ws:
    print(a)

else:
    print(-1)
