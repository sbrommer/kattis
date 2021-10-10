from sys import stdin

n = int(stdin.readline())

xs = set(map(int, stdin.readline().split()))
ys = set(map(int, stdin.readline().split()))

print(list(xs - ys)[0])
