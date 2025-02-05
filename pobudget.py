N = int(input())
budget = 0

for _ in range(N):
    input()
    budget += int(input())

print('Usch, vinst' if budget > 0 else
      'Nekad'       if budget < 0 else
      'Lagom')
