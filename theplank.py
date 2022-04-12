def subsetsum(n):
    # initialise memoisation array
    memo = [0] * (n + 1)
    memo[0] = 1

    # get number of possibilities per length
    for i in range(n + 1):
        for j in [1, 2, 3]:
            if i >= j:
                memo[i] += memo[i - j]

    return memo[n]

n = int(open(0).readline())

print(subsetsum(n))
