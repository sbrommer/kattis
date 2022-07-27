def h_words(puzzle):
    words = set()
    for p in puzzle:
        words.update(filter(lambda w: len(w) >= 2,
                            p.split('#')))
    return words


R = int(input().split()[0])

puzzle = [input() for _ in range(R)]

puzzle_T = map(''.join, zip(*puzzle))

words = h_words(puzzle).union(h_words(puzzle_T))

print(min(words))
