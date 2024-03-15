N = int(input())

G = [[int(n) for n in input().split()] for _ in range(N)]


print(sum(G[a][b] and G[b][c] and G[c][a]
      for a in range(N)
      for b in range(a+1, N)
      for c in range(b+1, N)))
