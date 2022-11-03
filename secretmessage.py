from math import ceil, sqrt

n = int(input())

for _ in range(n):
    original = input()

    l = len(original)
    m = ceil(sqrt(l)) ** 2
    k = int(sqrt(m))

    original += '*' * (m-l)

    secret = ''
 
    for c in range(k):
        for r in range(k):
            secret += original[(k-r-1)*k+c]

    secret = ''.join(list(filter(lambda c: c != '*', secret)))

    print(secret)
