from statistics import mean

_, p, _, *bag = open(0).readlines()

print('Jebb' if
      mean(item == 'ekki plast\n' for item in bag) <= float(p) else
      'Neibb')
