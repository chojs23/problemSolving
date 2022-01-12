from collections import defaultdict


def solution(tickets):
    answer = []

    routes = defaultdict(list)
    for ticket in tickets:
        routes[ticket[0]].append(ticket[1])
    for key in routes.keys():
        routes[key].sort(reverse=True)
    print(routes)
    stack = ["ICN"]
    path = []
    while stack:
        now = stack[-1]
        if not routes[now]:
            answer.append(stack.pop())
        else:
            stack.append(routes[now].pop())
    answer.reverse()
    return answer
