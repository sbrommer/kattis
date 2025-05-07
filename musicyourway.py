def readline():
    return input().split()


attributes = readline()

m = int(input())
songs = [readline() for _ in range(m)]
n = int(input())

for _ in range(n):
    sort_type = input()
    ix = attributes.index(sort_type)
    songs = sorted(songs, key=lambda song: song[ix])

    print(*attributes)
    for song in songs:
        print(*song)
    print()
