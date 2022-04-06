def mean(xs):
    return sum(xs) / len(xs)

s = open(0).readline()[:-1]

print(chr(int(mean([ord(c) for c in s]))))
