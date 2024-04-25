def rng(s):
    return s + s // 13 + 15


def dist(a, b):
    return abs(a % 10 - b % 10) + abs(a // 10 - b // 10)


s, *guesses = [int(n) for n in open(0).readlines()]

wumpusses = set()

while len(wumpusses) < 4:
    s = rng(s)
    wumpusses |= {s % 100}

for guess in guesses:
    if guess in wumpusses:
        wumpusses -= {guess}
        print('You hit a wumpus!')

    if wumpusses:
        print(min(map(lambda wumpus: dist(guess, wumpus), wumpusses)))

print(f'Your score is {len(guesses)} moves.')
