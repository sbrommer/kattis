l = input()

if ':)' in l and ':(' in l:
    print('double agent')
elif ':)' in l:
    print('alive')
elif ':(' in l:
    print('undead')
else:
    print('machine')
