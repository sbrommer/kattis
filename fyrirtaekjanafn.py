vowels = 'aeiouyAEIOUY'

S = input()

print(''.join(filter(lambda s: s in vowels, S)))
