from operator import not_

# her good answers
k = int(input())

my_answers = input()
her_answers = input()

same_answers = [a == b for (a, b) in zip(my_answers, her_answers)]

n = len(her_answers) # total answers
s = sum(same_answers) # same answers
d = sum(map(not_, same_answers)) # different answers

print(min(s, k) + min(n - k, d))
