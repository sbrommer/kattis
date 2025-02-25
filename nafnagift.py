from functools import cache

A, B = input(), input()


# Memoize length of shortest common subsequence
@cache
def scs(i, j):
    if not i:
        return j
    if not j:
        return i

    if A[i-1] == B[j-1]:
        return scs(i-1, j-1) + 1

    return min(scs(i-1, j), scs(i, j-1)) + 1


# Fill bottom-up
for i in range(len(A)+1):
    for j in range(len(B)+1):
        scs(i, j)

# Construct name top-down
i, j = len(A), len(B)
name = ''

while i and j:
    if A[i-1] == B[j-1]:
        name = A[i-1] + name
        i -= 1
        j -= 1
    elif scs(i-1, j) < scs(i, j-1):
        name = A[i-1] + name
        i -= 1
    else:
        name = B[j-1] + name
        j -= 1

name = A[:i] + B[:j] + name

print(name)
