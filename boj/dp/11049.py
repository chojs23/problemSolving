from sys import stdin

input = stdin.readline

N = int(input())
dp = [[0] * N for i in range(N)]

mat = []
for i in range(N):
    mat.append(list(map(int, input().rsplit())))

for i in range(1, N):
    for j in range(N - i):
        if i == 1:  # 차이가 1밖에 나지 않는 칸
            dp[j][j + i] = mat[j][0] * mat[j][1] * mat[j + i][1]
            continue
        dp[j][j + i] = 2**32  # 최댓값을 미리 넣어줌
        for k in range(j, j + i):
            dp[j][j + i] = min(
                dp[j][j + i],
                dp[j][k] + dp[k + 1][j + i] + mat[j][0] * mat[k][1] * mat[j + i][1],
            )

print(dp[0][N - 1])
