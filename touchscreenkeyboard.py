keyboard = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']

# Get location of a character on the keyboard.
def location(c):
	y = list(map(lambda r: c in r, keyboard)).index(True)
	x = keyboard[y].index(c)
	return x, y

# Get distance between two characters.
def distance1(c1, c2):
	x1, y1 = location(c1)
	x2, y2 = location(c2)
	return abs(x2 - x1) + abs(y2 - y1)

# Get distance between two words.
def distance(w1, w2):
	return sum(distance1(c1, c2) for c1, c2 in zip(w1, w2))

# Get number of cases.
o = open(0)
t = int(o.readline())

# Solve cases.
for _ in range(t):
	# Get string and number of words.
	s, l = o.readline().split()

	# Get distances of every word to the string.
	dists = dict()
	for _ in range(int(l)):
		w = o.readline().strip()
		dists[w] = distance(s, w)

	# Sort all words.
	ws = list(dists.keys())
	ws.sort()
	ws.sort(key = lambda w: dists[w])

	# Print words.
	for w in ws:
		print(w, dists[w])