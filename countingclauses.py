from sys import stdin

m = int(stdin.readline().split()[0])

print('unsatisfactory' if m < 8 else 'satisfactory')
