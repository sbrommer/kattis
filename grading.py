from sys import stdin

limits = list(map(int, stdin.readline().split()))
grade = int(stdin.readline())

i = sum(map(lambda l : l > grade, limits))

print('ABCDEF'[i])
