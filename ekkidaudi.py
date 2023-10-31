words1 = input().split('|')
words2 = input().split('|')

print(' '.join(w1 + w2 for w1, w2 in zip(words1, words2)))
