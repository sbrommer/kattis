o = open(0)

def readstring():
    return [int(c) for c in o.readline().strip()]

s1 = readstring()
s2 = readstring()

n = sum(t[0] != t[1] for t in zip(s1, s2))

print(2 ** n)
