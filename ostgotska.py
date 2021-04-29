from sys import stdin

words = stdin.readline().split()

aes = list(filter(lambda word : 'ae' in word, words))

if len(aes) / len(words) >= .4:
    print('dae ae ju traeligt va')
else:
    print('haer talar vi rikssvenska')
