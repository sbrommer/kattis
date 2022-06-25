T = int(input())

for _ in range(T):
    n = int(input())
    print(len(set(input() for _ in range(n))))
