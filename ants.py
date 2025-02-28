# It doesn't really matter whether the ants
# meet and turn. For an observer, this is
# similar to ants simply passing when meeting.
# So for the earliest moment, all ants walk to
# the nearest end, and for the latest moment,
# all ants walk to the furthest end.

xs = [int(x)
      for line in open(0).readlines()
      for x in line.split()]

t, *xs = xs

for _ in range(t):
    (l, n), xs = xs[:2], xs[2:]
    ants, xs = xs[:n], xs[n:]

    print(max(min(a, l-a) for a in ants),
          max(max(a, l-a) for a in ants))
