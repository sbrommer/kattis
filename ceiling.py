from functools import reduce


def readints():
    return [int(n) for n in input().split()]


def make_tree(ns):
    return reduce(insert, ns, [])


def insert(tree, data):
    if not tree:
        return [None, data, None]

    if data < tree[1]:
        tree[0] = insert(tree[0], data)

    else:
        tree[2] = insert(tree[2], data)

    return tree


def shape(tree):
    if not tree:
        return '*'

    return '[' + shape(tree[0]) + shape(tree[2]) + ']'


n, _ = readints()
trees = [make_tree(readints()) for _ in range(n)]
shapes = set(map(shape, trees))

print(len(shapes))
