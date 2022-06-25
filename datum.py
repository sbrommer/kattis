days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

months = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

d, m = map(int, input().split())

day = 3 + d + months[m-1]

print(days[day % 7])
