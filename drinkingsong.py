N = int(input())
beverage = input()

for n in range(N, 1, -1):
    s = 's' if n - 1 > 1 else ''
    print(f'{n} bottles of {beverage} on the wall, {n} bottles of {beverage}.')
    print(f'Take one down, pass it around, {n-1} bottle{s} of {beverage} on the wall.')
    print()

print(f'1 bottle of {beverage} on the wall, 1 bottle of {beverage}.')
print(f'Take it down, pass it around, no more bottles of {beverage}.')
