T = int(input())

for _ in range(T):
    N = input()

    print(max(bin(int(N[:i])).count('1') for i in range(1, len(N) + 1)))
