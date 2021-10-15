from sys import stdin
from operator import not_

# her good answers
k = int(stdin.readline())

my_answers = stdin.readline().strip()
her_answers = stdin.readline().strip()

same_answers = [a == b for (a, b) in zip(my_answers, her_answers)]

n = len(her_answers) # total answers
s = sum(same_answers) # same answers
d = sum(map(not_, same_answers)) # different answers

print(min(s, k) + min(n - k, d))
