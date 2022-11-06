from more_itertools import sliced

S = input()
code = input()

print(''.join(str(S[int(c) - 1]) for c in sliced(code, 3)))
