def readints():
    return [int(n) for n in input().split()]


_, k = readints()
a = readints()

i = a.index(k)

print('fyrst'      if i == 0 else
      'naestfyrst' if i == 1 else
      f'{i + 1} fyrst')
