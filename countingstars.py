def count_stars(pixels):
    def get_star(p):
        star = set()
        q = [p]
        while q:
            p, *q = q
            if p not in star:
                star |= {p}
                q += [p+d for d in [-1, 1, -1j, 1j] if p+d in pixels]
        return star

    stars = 0
    visited = set()

    for p in pixels:
        if p not in visited:
            stars += 1
            visited |= get_star(p)

    return stars


lines = open(0).readlines()
c = 0

while lines:
    c += 1
    mn, *lines = lines
    m, n = map(int, mn.split())
    image, lines = lines[:m], lines[m:]

    pixels = {x+y*1j
              for y, row in enumerate(image)
              for x, pixel in enumerate(row)
              if pixel == '-'}

    print(f'Case {c}: {count_stars(pixels)}')
