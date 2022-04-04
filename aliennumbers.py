o = open(0)

T = int(o.readline())

for c in range(T):
	# Get input
	n_s, s, t = list(o.readline().split())

	# Base s to base 10
	n_10 = 0
	for i in map(s.index, n_s):
		n_10 *= len(s)
		n_10 += i

	# Base 10 to base t
	n_t = []
	while n_10 > 0:
		n_t.insert(0, t[n_10 % len(t)])
		n_10 //= len(t)

	# Print answer
	print('Case #', c + 1, ': ', ''.join(n_t), sep='')