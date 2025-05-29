from operator import add

def readints():
    return map(int, input().split())


def solve(prices, X):
    if len(prices) <= 1:
        return len(prices)

    for i, (p1, p2) in enumerate(zip(prices, prices[1:]), 1):
        if p1 + p2 > X:
            return i

    return i+1

_, X = readints()
prices = sorted(readints())

print(solve(prices, X))
