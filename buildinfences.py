N = int(input())

cs = [map(int, input().split()) for _ in range(N)]

xs, ys = zip(*cs)

print(2 * (max(xs) - min(xs) + max(ys) - min(ys)) + 8)
