n, *vs = [int(i) for i in input().split()]

Vs = [vs[-1]]

while len(set(vs)) > 1:
    vs = [v - u for u, v in zip(vs, vs[1:])]
    Vs += [vs[-1]]

print(len(Vs) - 1, sum(Vs))
