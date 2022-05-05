N = int(input())
H = N // 2

ps = [int(p) for p in input().split()]
ps.sort(reverse=True)

print(sum(ps[:H]) + (sum(ps[H:]) - H) // 2)
