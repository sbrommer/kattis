def wheretoeat():
    n = int(input())

    for _ in range(n):
        k = int(input())
        restaurant = input()
        if {'pea soup', 'pancakes'} <= {input() for _ in range(k)}:
            return restaurant

    return 'Anywhere is fine I guess'


print(wheretoeat())
