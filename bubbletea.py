def readints():
    return [int(n) for n in input().split()]


N, = readints()
p_tea = readints()
M, = readints()
p_top = [0] + readints()
tops_per_tea = [readints()[1:] for _ in range(N)]
X, = readints()

p_top_min = [min(p_top[t] for t in tops) for tops in tops_per_tea]
p_tea_min = [p_tea + p_top for p_tea, p_top in zip(p_tea, p_top_min)]
p_min = min(p_tea_min)

print(max(0, X // p_min - 1))
