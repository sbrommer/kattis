def name(A, B):
    if not A:
        return B

    if not B:
        return A

    names = [A[0] + name(A[1:], B),
             B[0] + name(A, B[1:])]

    if A[0] == B[0]:
        names += [A[0] + name(A[1:], B[1:])]

    return min(names, key=len)


A = input()
B = input()

print(name(A, B))
