from collections import deque


def journey():
    bag = deque()

    for item in input():
        if item.islower():
            bag.append(item.upper())

        if item.isupper():
            safe = False

            while bag and not safe:
                safe = bag.pop() == item

            if not safe:
                return None

    return bag


bag = journey()

if bag is None:
    print('Neibb')
else:
    for item in 'PGO':
        print(bag.count(item))
