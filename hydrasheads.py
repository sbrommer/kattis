H, T = map(int, input().split())

while (H, T) != (0, 0):
    # Cut as many H as possible.
    S, H = divmod(H, 2)

    if H and not T:
        print(-1)

    else:
        # 'Uncut' the last H (if necessary).
        T += 2 * H
        S -= H

        # Add T until divisible by 4.
        t = -T % 4
        T += t
        S += t

        # Cut all T (3 cuts per 4 T).
        S += 3 * T // 4

        print(S)

    H, T = map(int, input().split())
