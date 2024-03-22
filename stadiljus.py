def locations(N, L, x, y):
    L = sorted(L)

    costs = 0
    for i, l in enumerate(sorted(L)):
        costs += L[i] * x
        budget = (i+1) * y
        if budget < costs:
            return i

    return N


N = int(input())
x = int(input())
y = int(input())
L = [int(n) for n in input().split()]

print(locations(N, L, x, y))
