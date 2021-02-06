import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

k = m // n

m_ = m - k*n                        

for _ in range(m_):
    print('*' * (k+1))

for _ in range(n - m_):
    print('*' * k)