from operator import mul

C = float(input())
L = int(input())
areas = [mul(*map(float, input().split())) for _ in range(L)]

print(C * sum(areas))
