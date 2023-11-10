def ordinals(n):
    return '{' + ','.join(map(ordinals, range(n))) + '}'


print(ordinals(int(input())))
