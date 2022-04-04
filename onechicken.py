from sys import stdin

n, m = list(map(int, stdin.readline().split()))

pq = m - n

if pq > 0:
    print('Dr. Chaz will have', str(pq), 'piece' + 's' * (pq != 1), 'of chicken left over!')
if pq < 0:
    print('Dr. Chaz needs', str(abs(pq)), 'more piece' + 's' * (pq != -1), 'of chicken!')