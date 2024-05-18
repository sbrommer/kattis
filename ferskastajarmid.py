memes = {name: int(con) * int(cool)
         for name, con, cool in
         [line.split() for line in open(0).readlines()[1:]]}

print(min(k for k, v in memes.items() if v == max(memes.values())))
