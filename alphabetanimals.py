letter = input()[-1]
n = int(input())
animals = [input() for _ in range(n)]


def play():
    best = ''
    for a in animals:
        if a[0] == letter:
            if not any(b for b in animals if a != b and a[-1] == b[0]):
                return a + '!'
            best = best or a
    return best or '?'


print(play())
