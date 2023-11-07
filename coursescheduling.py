requests = set(r.strip() for r in open(0).readlines()[1:])

requests = [r.split()[-1] for r in requests]

for course in sorted(list(set(requests))):
    print(course, requests.count(course))

