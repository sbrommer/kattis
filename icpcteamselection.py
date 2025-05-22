t = int(input())

for _ in range(t):
    N = int(input())
    Ps = sorted(map(int, input().split()))
    print(sum(Ps[N::2]))
