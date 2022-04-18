o = open(0)

n = int(o.readline())
notes = o.readline().split()

pitches = 'GFEDCBAgfedcba'
lines = 'FDBgea'


def get_duration(note):
    pitch = note[0]
    duration = 1 if len(note) == 1 else int(note[1:])
    return pitch * duration


notes = ' '.join([get_duration(note) for note in notes])

for pitch in pitches:
    default = '-' if pitch in lines else ' '

    print(pitch, ': ',
          ''.join(['*' if note == pitch else default for note in notes]),
          sep='')
