def readints():
    return [int(n) for n in input().split()]


def parse_case():
    n = readints()[0]

    prizes = [(prize[1:-1], prize[-1]) for prize in
              [readints() for _ in range(n)]]

    stickers = {t + 1: n for t, n in enumerate(readints())}

    return prizes, stickers


def value(prizes, stickers):
    return sum(min(stickers[t] for t in T) * cash for T, cash in prizes)


n_cases = readints()[0]

for i in range(n_cases):
    print(value(*parse_case()))
