n, m, k = map(int, input().split())
mines = {tuple(map(int, input().split())) for _ in range(k)}

for r in range(n):
    print(''.join('*' if (r+1, c+1) in mines else '.'
          for c in range(m)))
