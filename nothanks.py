input()
cards = sorted(list(map(int, input().split())))

previous = cards[0]
score = previous

for card in cards:
    score += card * (card > previous + 1)
    previous = card

print(score)
