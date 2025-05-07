from re import findall

n, m = map(int, findall(r'(\d+)', input()))

if n < m:
    print('<')
elif n > m:
    print('>')
else:
    print('Goggi svangur!')
