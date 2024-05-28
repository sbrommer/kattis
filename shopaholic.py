input()
ps = sorted([int(p) for p in input().split()], reverse=True)

print(sum(ps[2::3]))
