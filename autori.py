import sys

def isupper(c):
    return c.isupper()

long_var = sys.stdin.readline()
short_var = "".join(filter(isupper, long_var))

print(short_var)

