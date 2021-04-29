from sys import stdin

T = int(stdin.readline())

for i in range(T):
    print('Test', i+1)

    R = int(stdin.readline().split()[0])

    img = []
    for r in range(R):
        row = list(stdin.readline().strip())
        row.reverse()
        img.insert(0, ''.join(row))

    for row in img:
        print(''.join(row))
