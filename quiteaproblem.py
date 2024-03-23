for line in open(0).readlines():
    line = line.lower()
    print('yes' if 'problem' in line else 'no')
