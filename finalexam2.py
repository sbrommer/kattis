from operator import eq

answers = open(0).readlines()[1:]

print(sum(map(eq, answers, answers[1:])))
