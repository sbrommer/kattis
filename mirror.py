T = int(input())

for i in range(T):
    print('Test', i + 1)

    R = int(input().split()[0])

    print(*[input()[::-1] for r in range(R)][::-1])
