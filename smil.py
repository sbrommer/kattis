from sys import stdin
from math import sqrt
import re

s = stdin.readline().strip()

for smile in [':\)', ';\)', ':-\)', ';-\)']:
    for i in [pos.start() for pos in re.finditer(smile, s)]:
        print(i)
