def arithmetic(seq):
    Δs = [s2 - s1 for (s1, s2) in zip(seq, seq[1:])]
    return len(set(Δs)) == 1


o = open(0)

n = int(o.readline())

for _ in range(n):
    seq = [int(i) for i in o.readline().split()][1:]

    if arithmetic(seq):
        print('arithmetic')

    elif arithmetic(sorted(seq)):
        print('permuted arithmetic')

    else:
        print('non-arithmetic')
