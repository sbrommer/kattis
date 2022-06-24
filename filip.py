def read(s):
    return int(s[::-1])


print(max(*map(read, input().split())))
