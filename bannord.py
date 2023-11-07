S = set(input())
M = input()

for m in M.split():
    print(m if S.isdisjoint(set(m)) else '*' * len(m),
          end=' ')
