from sys import stdin

COCONUT  = 2
PALMUP   = 1
PALMDOWN = 0

s, n = list(map(int, stdin.readline().split()))

hands = [[p+1, COCONUT] for p in range(n)]

i = 0
while len(hands) > 1:
    i = (i + s - 1) % len(hands)
    player, state = hands[i]

    # Crack
    if state == COCONUT:
        hands[i] = [player, PALMUP]
        hands.insert(i, [player, PALMUP])

    # Milk
    elif state == PALMUP:
        hands[i] = [player, PALMDOWN]
        i += 1

    # Back
    else:
        del hands[i]

print((hands[0][0]))
