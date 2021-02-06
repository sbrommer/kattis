from sys import stdin

case = 0

alters = {'A#' : 'Bb',
          'Bb' : 'A#',
          'C#' : 'Db',
          'Db' : 'C#',
          'D#' : 'Eb',
          'Eb' : 'D#',
          'F#' : 'Gb',
          'Gb' : 'F#',
          'G#' : 'Ab',
          'Ab' : 'G#',}

for line in stdin.readlines():
    case += 1
    print('Case ' + str(case) + ':', end=' ')

    (note, tonality) = line.split()

    if len(note) == 1:
        print('UNIQUE')

    else:
        print(alters[note], tonality)
