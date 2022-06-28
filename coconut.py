COCONUT = 2
PALMUP = 1
PALMDOWN = 0

s, n = map(int, input().split())

hands = [[p + 1, COCONUT] for p in range(n)]

i = 0
while len(hands) > 1:
    # next hand
    i = (i + s - 1) % len(hands)
    player, state = hands[i]

    # crack
    if state == COCONUT:
        hands[i] = [player, PALMUP]
        hands.insert(i, [player, PALMUP])

    # milk
    elif state == PALMUP:
        hands[i] = [player, PALMDOWN]
        i += 1

    # back
    else:
        del hands[i]

print(hands[0][0])
