T = int(input())

for _ in range(T):
    n = int(input())
    votes = [int(input()) for _ in range(n)]
    n_win = max(votes)

    if votes.count(n_win) > 1:
        print('no winner')

    else:
        print('majority' if n_win > sum(votes) / 2 else 'minority', end=' ')
        print(f'winner {votes.index(n_win) + 1}')
