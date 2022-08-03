def dfs(depth, t):
    global cnt
    if depth == N:
        cnt += 1
        return
    for i in range(N):
        if check[i] or t+nums[i]-K < 0:
            continue
        check[i] = 1
        dfs(depth+1, t+nums[i]-K)
        check[i] = 0


N, K = map(int, input().split())
nums = list(map(int, input().split()))
check, cnt = [0]*N, 0
dfs(0, 0)
print(cnt)
