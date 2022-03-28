def solution(triangle):
    answer = 0
    # dp[i][j]=max(dp[i-1][j],
    if len(triangle) == 1:
        return triangle[0][0]
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0 or j == len(triangle[i]) - 1:
                if j == 0:
                    triangle[i][j] += triangle[i - 1][0]
                    continue
                triangle[i][j] += triangle[i - 1][j - 1]
            else:
                triangle[i][j] += max(triangle[i - 1][j - 1], triangle[i - 1][j])

    # print(triangle)
    return max(triangle[-1])
