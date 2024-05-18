n = int(input())
d = float(input())


def efficiency(v, r):
    time = d / v
    rate_of_fuel = r / time
    return v / rate_of_fuel


racers = {initials: (float(v), float(r)) for initials, v, r in
          [input().split() for _ in range(n)]}

print(max(racers, key=lambda r: efficiency(*racers.get(r))))
