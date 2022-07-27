def mean(xs):
    return sum(xs) / len(xs)


s = input()

print(chr(int(mean([ord(c) for c in s]))))
