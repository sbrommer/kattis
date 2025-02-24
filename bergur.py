N = int(input())
a = [int(ai) for ai in input().split()][::-1]

for i in range(1, N):
    a[i] = min(a[i], a[i-1])

print(sum(a))
