from collections import defaultdict

N = int(input())
Hs = [*map(int, input().split())]

arrows = defaultdict(int)
shots = 0

for H in Hs:
    if arrows[H]:
        arrows[H] -= 1
    else:
        shots += 1
    arrows[H-1] += 1

print(shots)
