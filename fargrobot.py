N = int(input())
letters = input()

while N:
    seen = set()
    while len(seen) < 3:
        letter, *letters = letters
        seen |= {letter}
    print(letter, end='')
    N -= 1
