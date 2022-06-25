def n(problem):
    ps = [int(p) for p in problem]
    return ps[-1] - ps[0] + 1


print(sum(map(lambda p: n(p.split('-')), input().split(';'))))
