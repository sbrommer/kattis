n, x = map(int, input().split())

for _ in range(n):
    x -= int(input())

print('Jebb' if x >= 0 else 'Neibb')
