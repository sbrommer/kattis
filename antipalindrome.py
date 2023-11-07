import re


def adjacent(string):
    return bool(re.search(r'(.)\1', string))


def palindrome(line):
    return adjacent(line) or \
           adjacent(line[::2]) or \
           adjacent(line[1::2])


line = input().replace(' ', '').lower()

print('Palindrome' if palindrome(line) else 'Anti-palindrome')
