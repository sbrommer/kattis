o = open(0)

n1 = int(o.readline())
n2 = int(o.readline())

cw = (n2 - n1) % 360
ccw = (n1 - n2) % 360

print(cw if cw <= ccw else -ccw)
