from sys import stdin

def readint():
    return int(stdin.readline())

n = readint()

books = []
for _ in range(n):
    books.append(readint())

books.sort(reverse=True)

price = 0
for i in range(n):
    price += books[i] * (i % 3 != 2)

print(price)