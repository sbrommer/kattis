from math import pi as π

d, a, b, h = map(int, open(0).readlines())

mahjong = π * (d / 2) ** 2
trapizza = (a + b) * h / 2

print('Trapizza!' if trapizza > mahjong else
      'Mahjong!' if mahjong > trapizza else
      'Jafn storar!')
