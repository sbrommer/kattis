def valid(P, S):
    if not P:
        return True

    if not S:
        return False

    if P[0] == S[0]:
        return valid(P[1:], S[1:])

    if S[0] in P:
        return False

    return valid(P, S[1:])


P, S = input().split()

print('PASS' if valid(P, S) else 'FAIL')
