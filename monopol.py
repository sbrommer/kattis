ns = {2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 8: 5, 9: 4, 10: 3, 11: 2, 12: 1}

ps = {k: v / 36 for k, v in ns.items()}

N = int(input())
As = set(map(int, input().split()))

print(sum(map(ps.get, As)))
