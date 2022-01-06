from collections import deque


def solution(people, limit):
    boat = 0
    people.sort()

    # 보트는 2명씩만 탈 수 있고 무게 제한도 있음.
    q = deque(people)

    while q:
        if len(q) >= 2:
            if q[0] + q[-1] <= limit:
                q.pop()
                q.popleft()
                boat += 1
            else:
                q.pop()
                boat += 1
        else:
            q.pop()
            boat += 1
    return boat
