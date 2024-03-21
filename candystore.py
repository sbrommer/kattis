from collections import defaultdict

NQ, *lines = open(0).readlines()
N, Q = [int(n) for n in NQ.split()]

customers = defaultdict(set)

for name in lines[:N]:
    initials = ''.join(word[0] for word in name.split())
    customers[initials].add(name.strip())

for initials in lines[N:]:
    matches = customers[initials.strip()]
    print('nobody' if not matches else
          'ambiguous' if len(matches) > 1 else
          list(matches)[0])
