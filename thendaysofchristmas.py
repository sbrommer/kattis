N = int(input())

sums = [sum(range(n+1)) for n in range(N+1)]

print(sums[-1], sum(sums))
