from collections import Counter

n = int(input())

for _ in range(n):
    # parse info
    print(input())

    buildings = input()
    b = int(buildings.split()[0])
    print(buildings)

    # get house numbers
    numbers = []

    while len(numbers) < b:
        l, *line = input().split()
        if l == '+':
            f, t, i = map(int, line)
            numbers += list(range(f, t + i, i))
        else:
            numbers += [int(l)]

    # get counter
    numbers = ''.join(map(str, numbers))
    counter = Counter(numbers)

    # print in correct format
    for k in range(10):
        print(f'Make {counter[str(k)]} digit {k}')
    total = sum(counter.values())
    print(f'In total {total} digit' + ('s' if total > 1 else ''))
