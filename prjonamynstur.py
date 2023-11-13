yarn_per_stitch = {'.': 20, 'O': 10, '\\': 25, '/': 25,
                   'A': 35, '^': 5,  'v': 22}

n = int(input().split()[0])

print(sum(sum(yarn_per_stitch[stitch]
          for stitch in input())
      for _ in range(n)))
