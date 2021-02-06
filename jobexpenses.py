from sys import stdin

stdin.readline()

ks = map(int, stdin.readline().split())
ks = filter(lambda k : k < 0, ks)

print(-sum(ks))
