N = int(input())


def readints():
    return list(map(int, input().split()))


# initialise
min_boil = 0
max_boil = 1000

# get possible boiling minutes
for _ in range(N):
    a, b = readints()

    min_boil = max(min_boil, a)
    max_boil = min(max_boil, b)

# answer
print('gunilla has a point' if min_boil <= max_boil else 'edward is right')
