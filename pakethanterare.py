# parse basics
t = int(input().split()[0])
ts = map(int, input().split())

# parse package versions
packages = dict()

for _ in range(t):
    p, v = input().split()
    packages[p] = int(v)

# calculate steps per store
for t in ts:
    s = 0
    for _ in range(t):
        p, v = input().split()
        s += packages[p] - int(v)
    print(s)
