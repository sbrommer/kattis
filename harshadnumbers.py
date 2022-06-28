def harshad(n):
    sod = sum(map(int, str(n)))
    return not n % sod


n = int(input())

while not harshad(n):
    n += 1

print(n)
