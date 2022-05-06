try:
    while input():
        # read and parse input
        codomain = input().split()[1:]

        n = int(input())
        mappings = [input().split(' -> ') for _ in range(n)]
        mappings = list(set(tuple(m) for m in mappings))  # remove doubles

        xs, ys = zip(*mappings)

        # get characteristics
        function = len(xs) == len(set(xs))
        injective = len(ys) == len(set(ys))
        surjective = set(ys) == set(codomain)

        # print result
        if not function:
            print('not a function')

        elif injective and surjective:
            print('bijective')

        elif injective:
            print('injective')

        elif surjective:
            print('surjective')

        else:  # not (injective or surjective)
            print('neither injective nor surjective')

except EOFError:
    pass
