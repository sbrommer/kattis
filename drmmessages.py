def rotate(m):
    v = sum(m)
    return list(map(lambda c: (c + v) % 26, m))

# Get input
m = input()

# To values
m = list(map(lambda c: ord(c) - ord('A'), m))

# Rotate
l = len(m) // 2
ml = rotate(m[:l])
mr = rotate(m[l:])

# Combine
for i in range(l):
    ml[i] = (ml[i] + mr[i]) % 26

# To string
m = map(lambda c: chr(c + ord('A')), ml)

print(''.join(m))
