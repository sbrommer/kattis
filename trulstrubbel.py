score = {'T': 0, 'H': 0}
notes = input()

for winner in notes:
    score[winner] += 1
    if any(s >= 11 for s in score.values()) and \
       abs(score['T'] - score['H']) >= 2:
        score = {'T': 0, 'H': 0}

print(f'{score["T"]}-{score["H"]}')
