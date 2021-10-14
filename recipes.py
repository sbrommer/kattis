from sys import stdin

T = int(stdin.readline())

for t in range(T):
    R, P, D = list(map(int, stdin.readline().split()))

    print('Recipe #', t+1)

    f = D / P

    # Get ingredients
    ingredients = []
    for _ in range(R):
        n, w, p = stdin.readline().split()
        w = float(w)
        p = float(p)

        ingredients.append((n, w, p))

    # Calculate weights
    W = [i[1] for i in ingredients if i[2] == 100][0]

    for i in ingredients:
        print(i[0], i[2] * W * f / 100)

    print('-' * 40)
