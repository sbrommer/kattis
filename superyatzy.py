from collections import Counter

N, M = map(int, input().split())

dice = [int(input()) for _ in range(N)]

counter = Counter(dice)

print('Ja' if max(counter.values()) + M >= N else 'Nej')
