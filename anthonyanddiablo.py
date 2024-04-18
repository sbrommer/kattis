from math import pi as π

A, N = map(float, input().split())

max_r = N / (2 * π)
max_A = π * max_r ** 2

print('Diablo is happy!'
      if max_A >= A else
      'Need more materials!')
