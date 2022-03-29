def solution(n, costs):
    ans = 0

    costs.sort(key=lambda x: x[2])  # cost 기준으로 오름차순 정렬
    routes = set([costs[0][0]])  # 집합
    print(routes)
    while len(routes) != n:
        for i, cost in enumerate(costs):
            if cost[0] in routes and cost[1] in routes:
                continue
            if cost[0] in routes or cost[1] in routes:
                routes.add(cost[0])
                routes.add(cost[1])
                # print(routes)
                ans += cost[2]
                costs[i] = [-1, -1, -1]
                break
    return ans
