def substring(F, H):
    if not F:
        return True

    if not H:
        return False

    if F[0] == H[0]:
        return substring(F[1:], H[1:])

    if F[0] != H[0]:
        return substring(F, H[1:])


F, H = input(), input()

print('Ja' if substring(F, H) else 'Nej')
