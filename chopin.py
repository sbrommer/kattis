o = open(0)

case = 1

alters = {'A#': 'Bb',
          'Bb': 'A#',
          'C#': 'Db',
          'Db': 'C#',
          'D#': 'Eb',
          'Eb': 'D#',
          'F#': 'Gb',
          'Gb': 'F#',
          'G#': 'Ab',
          'Ab': 'G#'}

for line in o.readlines():
    print('Case', str(case) + ':')

    note, tonality = line.split()

    if len(note) == 1:
        print('UNIQUE')

    else:
        print(alters[note], tonality)

    case += 1
