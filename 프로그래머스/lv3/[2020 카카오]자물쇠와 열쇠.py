import copy


def rotate(matrix):
    # reverse
    l = 0
    r = len(matrix) - 1
    while l < r:
        matrix[l], matrix[r] = matrix[r], matrix[l]
        l += 1
        r -= 1
    # transpose
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def check(new_lock):
    n = len(new_lock) // 3
    for i in range(n, n * 2):
        for j in range(n, n * 2):
            if new_lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    n = len(lock)
    m = len(key)
    # 3배 x 3배로 자물쇠 초기화
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]

    # 새로운 자물쇠 중간 부분에 기존 자물쇠 값 넣기
    for i in range(n):
        for j in range(n):
            new_lock[n + i][n + j] = lock[i][j]

    # 열쇠가 맞는 지 체크 - 모든 방향에 대해
    for _ in range(4):
        rotate(key)
        for x in range(n * 2):
            for y in range(n * 2):
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]
                # 맞는 지 검사
                if check(new_lock):
                    return True

                # 안 맞으면 열쇠 다시 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]
    return False
