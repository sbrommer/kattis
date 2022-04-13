# parse input
o = open(0)

n, s = list(map(int, o.readline().split()))


# get ounces of water per order
def get_water():
    order = o.readline()
    return int(order[0]) + (order[1] == 'L')


# initialise
tank = s
refills = 0

# run day
for _ in range(n):
    x = get_water()

    if tank < x:
        tank = s
        refills += 1

    tank -= x


# answer
print(refills)
