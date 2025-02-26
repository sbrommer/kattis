M = 10**9 + 7

inversions = 0
ones = 0
blanks = 0

for b in input():
    ones += b == '1'

    if b == '?':
        inversions *= 2

    if b in '0?':
        inversions += ones   * pow(2, blanks,     M) + \
                      blanks * pow(2, blanks - 1, M)

    blanks += b == '?'

    inversions %= M

print(inversions)
