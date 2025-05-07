cat = ''.join

values = [*map(int, input().split())]
maxs = cat('RGB'[i] for i, v in enumerate(values) if v == max(values))

colourmap = {
    'R': 'raudur', 'G': 'graenn', 'B': 'blar',
    'RG': 'gulur', 'RB': 'fjolubleikur',
    'GB': 'blagraenn', 'RGB': 'grar'
}

if all(v == 0 for v in values):
    print('svartur')
elif all(v == 255 for v in values):
    print('hvitur')
else:
    print(colourmap[maxs])
