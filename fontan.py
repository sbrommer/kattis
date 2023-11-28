N, M = map(int, input().split())

S = list(input())

for n in range(N - 1):
    # get next line
    T = list(input())

    # stone left to right
    for m in range(1, M):
        if S[m] == '.' and S[m-1] == 'V' and T[m-1] == '#':
            S[m] = 'V'

    # stone right to left
    for m in range(M-2, -1, -1):
        if S[m] == '.' and S[m+1] == 'V' and T[m+1] == '#':
            S[m] = 'V'

    # print current line
    print(''.join(S))

    # air
    for m in range(M):
        if T[m] == '.' and S[m] == 'V':
            T[m] = 'V'

    # set next line as current
    S = T

# print last line
print(''.join(S))
