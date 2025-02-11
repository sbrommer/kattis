angles = [int(input()) for _ in range(3)]

print('Ratvinklig' if 90 in angles else
      'Trubbig'    if any(a > 90 for a in angles) else
      'Spetsig', 'Triangel')
