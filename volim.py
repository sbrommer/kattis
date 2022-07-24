K = int(input())
N = int(input())

t = 0

for _ in range(N):
    T, Z = input().split()

    t += int(T)
    if t >= 3 * 60 + 30:
        break  # boom

    K += Z == 'T'

print(K % 8 or 8)
