def parse(bag):
    return int(bag.replace('5', '_').replace('2', '5').replace('_', '2')[::-1])


bags = [parse(bag) for bag in input().split()]

print(1 + bags.index(max(bags)))
