items = [item.strip() for item in open(0).readlines()[1:]]
kpw = ['keys', 'phone', 'wallet']

for item in kpw:
    if item not in items:
        print(item)

if set(kpw) <= set(items):
    print('ready')
