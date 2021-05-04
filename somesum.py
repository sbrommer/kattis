from sys import stdin

N = int(stdin.readline())

print('Either' if N % 2 else 'Odd' if N % 4 else 'Even')
