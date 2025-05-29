def bisect(x, lo, hi, key, ε):
    mid = lo + (hi - lo) / 2

    while x < key(mid-ε) or key(mid+ε) < x:
        if x < key(mid):
            hi = mid
        if key(mid) < x:
            lo = mid

        mid = lo + (hi - lo) / 2

    return mid
    


n = int(input())

print(bisect(n, 0, 10, lambda x: x**x, 1e-6))
