input()
xs = list(map(int, input().split()))

xs.sort(reverse = True)
alice = sum(xs[::2])
bob = sum(xs[1::2])

print(alice, bob)
