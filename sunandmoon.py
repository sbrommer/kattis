def readints():
    return [int(n) for n in input().split()]


def get_year(ds, ys, dm, ym):
    def get_year_(ds, dm):
        if ds < dm:
            return get_year_(ds + ys, dm)

        if dm < ds:
            return get_year_(ds, dm + ym)

        return ds

    return get_year_(ds, dm)


ds, ys = readints()
dm, ym = readints()

print(get_year(-ds, ys, -dm, ym))
