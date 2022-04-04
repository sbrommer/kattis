from sys import stdin

def readsound():
    return stdin.readline().split()[-1]

t = int(stdin.readline())

for _ in range(t):
    recording = stdin.readline().split()

    sounds = set()
    sound = readsound()
    while sound != 'say?':
        sounds.add(sound)
        sound = readsound()

    fox = [sound for sound in recording if sound not in sounds]

    print(' '.join(fox))


