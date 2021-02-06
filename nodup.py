from sys import stdin

word_list = stdin.readline().split()
word_set = set(word_list)

print('yes' if len(word_list) == len(word_set) else 'no')
