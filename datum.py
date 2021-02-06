from sys import stdin

days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

months = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

(d, m) = list(map(int, stdin.readline().split()))

day = 3 + d + months[m-1]

print(days[day % 7])