b, d, c, l = [int(c) for c in open(0).readline().split()]

solution = False

for birds in range(l // b + 1):
    m = l - birds * b

    for dogs in range(m // d + 1):
        n = m - dogs * d

        if not n % c:
            solution = True
            print(birds, dogs, n // c)

if not solution:
    print('impossible')
