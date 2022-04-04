o = open(0)

def readints():
	return list(map(int, o.readline().split()))

n, p, k = readints()
p /= 100

ts = readints()
ts.append(k)

T = ts[0]
for i in range(1, n + 1):
	speed = 1 + i * p
	dt = ts[i] - ts[i - 1]
	T += dt * speed

print(T)