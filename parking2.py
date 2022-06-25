t = int(input())

for _ in range(t):
    input()
    xs = [int(x) for x in input().split()]

    print((max(xs) - min(xs)) * 2)
