start = input()
end = input()

print(1 + sum(s != e for s, e in zip(start, end)))
