from collections import defaultdict

o = open(0)

# Initialise
l = 1
n = int(o.readline())

while n:
    # Get animals
    animals = defaultdict(lambda: 0)

    for _ in range(n):
        animal = o.readline().split()[-1].lower()
        animals[animal] += 1

    # Print counts
    print('List ', l, ':', sep='')
    for animal, count in sorted(animals.items()):
        print(animal, '|', count)

    # Update
    l += 1
    n = int(o.readline())
