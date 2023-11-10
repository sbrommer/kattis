services = ['Monnei', 'Fjee', 'Dolladollabilljoll']
fees = [int(input()) for _ in range(3)]

print(services[fees.index(min(fees))])
