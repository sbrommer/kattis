n = int(input())

for _ in range(n):
    s = input().lower()
    print(s[0].upper() + s[1:].lower())
