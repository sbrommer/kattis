year = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN',
        'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']

dd, ism, enm, yy = input().split()

print(f'20{yy}-{year.index(enm[1:]) + 1:02d}-{dd}')
