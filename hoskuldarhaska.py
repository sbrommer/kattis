from itertools import product

n = int(input())
words = [sorted(input().split()[1:]) for _ in range(n)]

print(*map(' '.join, product(*words)), sep='\n')
