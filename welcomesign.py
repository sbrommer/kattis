r, c = map(int, input().split())
R = 0

for line in range(r):
    word = input()
    blanks = c - len(word)

    rem = blanks % 2
    blanks //= 2
    R = (R + rem) % 2

    l = blanks + rem * (1 - R)
    r = blanks + rem * R

    print('.' * l + word + '.' * r)
