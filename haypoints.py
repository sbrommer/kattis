from sys import stdin

(m, n) = list(map(int, stdin.readline().split()))

dictionary = {}

for _ in range(m):
    (word, value) = stdin.readline().split()
    value = int(value)
    dictionary[word] = value

for _ in range(n):
    salary = 0

    line = stdin.readline()[:-1]
    while line != '.':
        for word in line.split():
            if word in dictionary.keys():
                salary += dictionary[word]
        line = stdin.readline()[:-1]

    print(salary)
