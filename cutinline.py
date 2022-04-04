o = open(0)

# Get initial line.
line = []
N = int(o.readline())
for _ in range(N):
	line.append(o.readline().strip())

# Do all events.
C = int(o.readline())
for _ in range(C):
	event, *persons = o.readline().split()

	if event == 'leave':
		line.remove(persons[0])

	else: # event == 'cut'
		a, b = persons
		i = line.index(b)
		line = line[:i] + [a] + line[i:]

# Print resulting line.
for person in line:
	print(person)