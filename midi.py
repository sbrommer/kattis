n = int(input())

text = ''.join([input()[::-1] for _ in range(n)][::-1])

print(text)
