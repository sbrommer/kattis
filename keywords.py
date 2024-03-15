ks = open(0).readlines()[1:]
ks = set(k.replace('-', ' ').lower() for k in ks)

print(len(ks))
