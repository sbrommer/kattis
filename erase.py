from sys import stdin

n = int(stdin.readline())
m = n % 2 == 0

before = list(map(int, stdin.readline().strip()))
after = list(map(int, stdin.readline().strip()))

succeeded = True

for i in range(len(before)):
    if (before[i] == m) != after[i]:
        succeeded = False
        break

if succeeded:
    print('Deletion succeeded')
else:
    print('Deletion failed')
