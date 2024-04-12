def closest(cs, d):
    return min(cs, key=lambda c: abs(ord(d) - ord(c)))


hard = 'bcdgknpt'

words = input().split()

for word in words:
    # Get info
    syllables = word.split('-')
    l = len(syllables[0])
    up = word[0].isupper()
    word = list(''.join(syllables).lower())

    # All nimion words start with ‘hard’ consonants
    start = word[0] if word[0] in hard else closest(hard, word[0])
    word = [start] + word[1:]

    # Any hard consonant...
    word = word[:l] + [start if c in hard else c for c in word[l:]]

    # No word ends in a hard consonant
    if word[-1] in hard:
        word += [closest('aou', word[-1]), 'h']

    word = word[0].upper() + ''.join(word[1:]) if up else ''.join(word)
    print(word, end=' ')
