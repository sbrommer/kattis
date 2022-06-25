n, *ps = [int(l) for l in open(0).readlines()]

if n % 2:
    print('still running')

else:
    print(sum(ps[1::2]) - sum(ps[0::2]))
