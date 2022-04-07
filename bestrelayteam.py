# parse
o = open(0)
n = int(o.readline())

relayers = []
starters = []

for _ in range(n):
    runner, t_start, t_relay = o.readline().split()
    starters.append((runner, float(t_start)))
    relayers.append((runner, float(t_relay)))

relayers.sort(key = lambda r: r[1])

# search
best_time = 100
best_runners = []

for starter in starters:
    others = [r for r in relayers if r[0] != starter[0]][:3]
    runners = [starter] + others

    time = sum(r[1] for r in runners)

    if time < best_time:
        best_time = time
        best_runners = [r[0] for r in runners]

print(best_time, *best_runners, sep='\n')
