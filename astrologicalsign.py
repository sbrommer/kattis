from sys import stdin

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

signs = ['Capricorn', 'Aquarius', 'Pisces', 'Aries',
         'Taurus', 'Gemini', 'Cancer', 'Leo',
         'Virgo', 'Libra', 'Scorpio', 'Sagittarius']

next_sign = [21, 20, 21, 21, 21, 22,
             23, 23, 22, 23, 23, 22]

t = int(stdin.readline())

for _ in range(t):
    d, m = stdin.readline().split()
    d = int(d)
    m = months.index(m)

    print(signs[(m + (d >= next_sign[m])) % 12])
