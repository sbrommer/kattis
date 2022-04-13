# parse
o = open(0)


def readints():
    return list(map(int, o.readline().split()))


N, K = readints()
sequence = readints()

# count colours
colours = {colour: sequence.count(colour) for colour in range(1, K + 1)}

least_occurrence = min(colours.values())
possible_colours = [c for c, o in colours.items() if o == least_occurrence]

# answer
print(len(possible_colours))
print(*possible_colours)
