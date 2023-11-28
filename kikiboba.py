s = input()

b = s.count('b')
k = s.count('k')

if not b and not k:
    print('none')
elif b > k:
    print('boba')
elif k > b:
    print('kiki')
else:
    print('boki')
