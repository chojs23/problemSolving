import sys


def dfs(node, conn, visited):
    visited[node] = True
    children = [next_node for next_node in conn[node]
                if not visited[next_node]]
    pick, not_pick = 1, 0  # 나를 선택하는 경우,나를 선택하지 않는 경우

    if not children:  # leaf
        return (pick, not_pick)
    else:
        for child in children:
            child_pick, child_not_pick = dfs(child, conn, visited)
            # 자식을 고르지 않았으면 무조건 나를 골라야 함
            # 자식을 골랐다면 나를 골라도 되고 안골라도 됨
            pick += min(child_pick, child_not_pick)
            not_pick += child_pick
        return (pick, not_pick)


def solution(n, lighthouse):
    sys.setrecursionlimit(100000)

    answer = 0
    conn = [[]for _ in range(n+1)]
    for a, b in lighthouse:
        conn[a].append(b)
        conn[b].append(a)
    visited = [0 for _ in range(n+1)]

    root = 1
    result = dfs(root, conn, visited)
    return min(result)
