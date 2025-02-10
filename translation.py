input()
sentence = input().split()
M = int(input())
d = dict(input().split() for _ in range(M))

print(*[d[word] for word in sentence])
