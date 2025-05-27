from itertools import permutations

L = int(1e7)
cat = ''.join

prime = [0, 0] + [1] * L

for p in range(2, L):
    if prime[p]:
        for q in range(p*p, L, p):
            prime[q] = 0


c = int(input())

for _ in range(c):
    ds = input()
    ps = {int(cat(p)) for l in range(len(ds))
                      for p in permutations(ds, l+1)}

    print(sum(1 for p in ps if prime[p]))
