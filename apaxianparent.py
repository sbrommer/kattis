y, p = input().split()

if y[-2:] == 'ex':
    print(y + p)
else:
    if y[-1] in 'aeiou':
        y = y[:-1]
    print(y + 'ex' + p)
