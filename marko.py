from sys import stdin

keys = ['abc', 'def', 'ghi',
        'jkl', 'mno', 'pqrs',
        'tuv', 'wxyz']

def get_key(c):
    return list(map(lambda key : c in key, keys)).index(True) + 2

def get_keys(word):
    return ''.join(map(lambda c : str(get_key(c)), word))

N = int(stdin.readline())

t9 = list()
for _ in range(N):
    word = stdin.readline().strip()
    t9.append(get_keys(word))

S = stdin.readline().strip()
print(t9.count(S))
