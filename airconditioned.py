snd = lambda t: t[1]

N = int(input())

preferences = [tuple(map(int, input().split())) for _ in range(N)]
preferences = sorted(preferences, key=snd)

rooms = 0
t = 0

for L, U in preferences:
    if t < L:
        rooms += 1
        t = U

print(rooms)
