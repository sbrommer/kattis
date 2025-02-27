def parseints():
    return [int(n) for n in input().split()]


c, n = parseints()
songs = parseints()

c += 1
mem = [(w1+w2, abs(w1-w2))
       for w1 in range(c)
       for w2 in range(c)]

for song in songs:
    for w1 in range(c)[::-1]:
        for w2 in range(w1+1)[::-1]:
            if song <= w1:
                mem[w1*c+w2] = min(mem[w1*c+w2],
                                   mem[(max(w1-song, w2))*c+min(w1-song, w2)])

            if song <= w2:
                mem[w1*c+w2] = min(mem[w1*c+w2],
                                   mem[w1*c+w2-song])

c -= 1
s, d = mem[c*(c+1)+c]
print(c-(s-d)//2, c-(s+d)//2)
