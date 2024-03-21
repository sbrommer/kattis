boxes = [line.split() for line in open(0).readlines()[1:]]

print(sum(len(box) - len(set(box)) for box in boxes))
