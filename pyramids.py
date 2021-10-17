from sys import stdin

N = int(stdin.readline())

blocks = 0
for i in range(1, 1000, 2):
    print('side', i, 'area', i**2)
    blocks += i ** 2
    print('blocks', blocks, 'height', i / 2)
    if blocks > N:
        print(i / 2)
        break
