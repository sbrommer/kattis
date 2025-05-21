from re import findall
from collections import defaultdict


def parse_atoms(molecule, k=1):
    atoms = defaultdict(int)

    for a in findall(r'[A-Z]\d*', molecule):
        a, n = a[0], a[1:]
        atoms[a] += (int(n) if n else 1) * k

    return atoms


molecule, k = input().split()
atoms_in = parse_atoms(molecule, int(k))

molecule = input()
atoms_out = parse_atoms(molecule)

print(min(atoms_in[a] // n for a, n in atoms_out.items()))
