n = int(input())
ss = [int(s) for s in input().split()]

if max(ss) > sum(ss) - max(ss):
    print('impossible')

else:
    print(*[i + 1 for i in
            sorted(range(len(ss)), key=lambda i: ss[i], reverse=True)])
