t = int(input())

for _ in range(t):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    # S[i]는 1번부터 i번까지의 누적합
    S = [0 for _ in range(n + 1)]
    for i in range(1, n + 1):
        S[i] = S[i - 1] + arr[i]

    DP = [
        [0 for i in range(n + 1)] for _ in range(n + 1)
    ]  # DP[i][j]= i에서 j까지 합하는데 필요한 최소 비용
    for i in range(2, n + 1):  # 부분 파일의 길이
        for j in range(1, n + 2 - i):  # 시작점
            DP[j][j + i - 1] = min(
                [DP[j][j + k] + DP[j + k + 1][j + i - 1] for k in range(i - 1)]
            ) + (S[j + i - 1] - S[j - 1])
    print(DP[1][n])
