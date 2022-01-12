def solution(n, computers):
    def dfs(i):
        for com in range(n):
            if com != i and computers[i][com] == 1 and visited[com] == False:
                visited[com] = True
                dfs(com)

    answer = 0
    visited = [False] * n
    for i in range(n):
        if visited[i] == False:
            visited[i] = True
            dfs(i)
            answer += 1

    return answer
