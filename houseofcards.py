def triangular_nr(n):
    return n * (n+1) // 2


def cards(h):
    return triangular_nr(h) * 3 - h


h = int(input())

while cards(h) % 4:
    h += 1

print(h)
