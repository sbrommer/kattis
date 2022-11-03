n = int(input())
m = n % 2 == 0

before = list(map(int, input()))
after = list(map(int, input()))

succeeded = True

for i in range(len(before)):
    if (before[i] == m) != after[i]:
        succeeded = False
        break

if succeeded:
    print('Deletion succeeded')
else:
    print('Deletion failed')
