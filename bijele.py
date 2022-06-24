from operator import sub

pieces = list(map(int, input().split()))

print(*map(sub, [1, 1, 2, 2, 2, 8], pieces))
