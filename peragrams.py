s = input()

n_odd = sum(s.count(c) % 2 for c in set(s))

print(max(0, n_odd - 1))
