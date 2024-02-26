from itertools import combinations, starmap


def readfloats():
    return [float(n) for n in input().split()]


def ccw(A, B, C):
    return (C[1] - A[1]) * (B[0] - A[0]) > (B[1] - A[1]) * (C[0] - A[0])


def intersect(s1, s2):
    A, B = s1[:2], s1[2:]
    C, D = s2[:2], s2[2:]
    return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)


def is_triangle(s1, s2, s3):
    return intersect(s1, s2) and intersect(s1, s3) and intersect(s2, s3)


n = int(input())

while n:
    segments = [readfloats() for _ in range(n)]
    print(sum(starmap(is_triangle, combinations(segments, 3))))

    n = int(input())
