def desiigner(s):
    return len(s) >= 4 and \
           s[0] == 'b' and \
           s[-1] in 'aeiouy' and \
           len(set(s[1:-1])) == 1


print('Jebb' if desiigner(input()) else 'Neibb')
