import sys

input = sys.stdin.readline

N, B = map(int, input().rstrip().split())

matrix = []

for i in range(N):
    matrix.append(list(map(int, input().rstrip().rsplit())))


def power(matrix):
    ret = []
    for i in range(N):
        ret.append([0] * N)
    for i in range(N):
        for j in range(N):
            for k in range(N):
                ret[i][j] += matrix[i][k] * matrix[k][j]
            ret[i][j] %= 1000
    return ret


def mult(matrix1, matrix2):
    ret = []
    for i in range(N):
        ret.append([0] * N)
    for i in range(N):
        for j in range(N):
            for k in range(N):
                ret[i][j] += matrix1[i][k] * matrix2[k][j]

    return ret


def sol(matrix, time):
    if time == 1:
        return matrix
    if time % 2 == 0:
        return power(sol(matrix, time // 2))
    else:
        return mult(sol(matrix, time - 1), matrix)


ret = sol(matrix, B)
for i in range(N):
    for j in range(N):
        print(ret[i][j] % 1000, end=" ")
    print()
