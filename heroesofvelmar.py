cards = {
    'Shadow': 6,
    'Gale': 5,
    'Ranger': 4,
    'Anvil': 7,
    'Vexia': 3,
    'Guardian': 8,
    'Thunderheart': 6,
    'Frostwhisper': 2,
    'Voidclaw': 3,
    'Ironwood': 3,
    'Zenith': 4,
    'Seraphina': 1
}


def power_level(cs, location):
    power = sum(cards[c] for c in cs)

    for i, c in enumerate(cs):
        if c == 'Thunderheart' and len(cs) == 4:
            power += 6

        if c == 'Zenith' and location == 1:
            power += 5

        if c == 'Seraphina':
            power += len(cs) - 1

    return power


def location_power(l):
    p1, p2 = [power_level(input().split()[1:], l) for _ in range(2)]
    return p1 - p2


def signum(n):
    return 1 if n > 0 else -1 if n < 0 else 0


power_levels = [location_power(l) for l in range(3)]

winner = sum(map(signum, power_levels)) or sum(power_levels)

print('Player 1' if winner > 0 else
      'Player 2' if winner < 0 else
      'Tie')
