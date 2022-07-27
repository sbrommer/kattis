from operator import gt

N = int(input())
xs = list(map(int, input().split()))

t = 1 + sum(map(gt, xs[1:], xs))

print(t)
