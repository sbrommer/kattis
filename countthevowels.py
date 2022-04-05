s = open(0).readline().strip()

print(sum(c in 'aeiouAEIOU' for c in s))
