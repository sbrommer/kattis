input()
song = set(input().split())

notes = ['A', 'A#', 'B', 'C', 'C#', 'D',
         'D#', 'E', 'F', 'F#', 'G', 'G#']

major = [0, 2, 4, 5, 7, 9, 11]

scales = []
for n in range(12):
    scale = {notes[(m + n) % 12] for m in major}
    if song <= scale:
        scales.append(notes[n])

print(*scales or ['none'])
