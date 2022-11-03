def readints():
    return map(int, input().split())


def parse_tree():
    tree = {}

    A, *Bs = readints()
    while A >= 0:
        tree[A] = set(Bs)
        A, *Bs = readints()

    return tree


def parent(tree, node):
    for A, Bs in tree.items():
        if node in Bs:
            return A
    return -1


kitten, = readints()
tree = parse_tree()

while kitten >= 0:
    print(kitten)
    kitten = parent(tree, kitten)
