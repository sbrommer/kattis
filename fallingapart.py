from sys import stdin

stdin.readline()
xs = list(map(int, stdin.readline().split()))

xs.sort(reverse = True)
alice = sum(xs[::2])
bob = sum(xs[1::2])

print(alice, bob)
