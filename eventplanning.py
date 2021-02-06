import sys

(n, b, h, w) = list(map(int, sys.stdin.readline().split()))

c_min = b + 1

for _ in range(h):
    p = int(sys.stdin.readline())
    
    xs = list(map(int, sys.stdin.readline().split()))

    c = p*n

    if c < b and any(map(lambda x : x >= n, xs)):
        c_min = min(c_min, c)

if c_min > b:
    print('stay home')
else:
    print(c_min)