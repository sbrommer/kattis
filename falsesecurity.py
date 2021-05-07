from sys import stdin

c_to_m = {'A' : '.-'   , 'B' : '-...' , 'C' : '-.-.' ,
          'D' : '-..'  , 'E' : '.'    , 'F' : '..-.' ,
          'G' : '--.'  , 'H' : '....' , 'I' : '..'   ,
          'J' : '.---' , 'K' : '-.-'  , 'L' : '.-..' ,
          'M' : '--'   , 'N' : '-.'   , 'O' : '---'  ,
          'P' : '.--.' , 'Q' : '--.-' , 'R' : '.-.'  ,
          'S' : '...'  , 'T' : '-'    , 'U' : '..-'  ,
          'V' : '...-' , 'W' : '.--'  , 'X' : '-..-' ,
          'Y' : '-.--' , 'Z' : '--..' , '_' : '..--' ,
          ',' : '.-.-' , '.' : '---.' , '?' : '----'}

m_to_c = dict([(m, c) for (c, m) in c_to_m.items()])

line = stdin.readline().strip()

while line != '':
    morse = list(map(lambda c : c_to_m[c], line))

    lengths = list(map(len, morse))
    lengths.reverse()
    ix = [sum(lengths[:i]) for i in range(len(lengths))]

    morse = ''.join(morse)
    morse = [morse[i:j] for i,j in zip(ix, ix[1:] + [None])]

    line = map(lambda m : m_to_c[m], morse)
    line = ''.join(line)

    print(line)

    line = stdin.readline().strip()
