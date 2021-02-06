import sys

sys.stdin.readline()
at_bats = map(int, sys.stdin.readline().split())
officials = list(filter(lambda at_bat : at_bat >= 0, at_bats))
print(sum(officials) / len(officials))