def prime(p):
    if p <= 1:
        return False
    for d in range(2, int(p**0.5)+1):
        if not p % d:
            return False
    return True


n = int(input())

for _ in range(n):
    x = int(input())

    ps = [(p, x-p) for p in range(2, x//2+1) if prime(p) and prime(x-p)]

    print(f'{x} has {len(ps)} representation(s)')
    for p1, p2 in ps:
        print(f'{p1}+{p2}')

    print()
