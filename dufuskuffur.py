from re import findall

n, m = map(int, findall(r'\d+', open(0).read()))
if n == m:
    print('Dufur passa fullkomlega')
elif n < m:
    print('Dufur passa')
else:
    print('Dufur passa ekki')
