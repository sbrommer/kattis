s = input()

vowels = sum(c in 'aeiou' for c in s)
ys = sum(c == 'y' for c in s)

print(vowels, vowels + ys)
