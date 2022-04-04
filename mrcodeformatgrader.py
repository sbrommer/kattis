# Imports.
from itertools import groupby, count

# Functions.

## Format all lines.
def format(xs):
	# Create groups of successive lines.
	groups = groupby(sorted(xs), lambda n, c=count(): n - next(c))
	groups = [list(g) for _, g in groups]

	# Initial groups to string, and last group to string.
	init = ', '.join(map(pretty_str, groups[:-1]))
	last = pretty_str(groups[-1])

	# Join initial groups and last group.
	return (init + ' and ' if len(groups) > 1 else '') + last

## Format one group of successive lines.
def pretty_str(g):
	# First element to string.
	s = str(g[0])

	# Last element to string, if it exists.
	if len(g) > 1: s += '-' + str(g[-1])

	return s

# Read and parse data.
cn, errors = open(0).readlines()
c, n = list(map(int, cn.split()))

# Compute.
errors  = set(map(int, errors.split()))
correct = set(range(1, c + 1)) - errors

print('Errors:', format(errors))
print('Correct:', format(correct))