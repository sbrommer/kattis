import re

N = int(input())
rap = input()

print(max(int(n) for n in re.findall(r'\d+', rap)))
