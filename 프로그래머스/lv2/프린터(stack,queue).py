from collections import deque


def solution(priorities, location):
    answer = 0
    priolist = []
    wait = deque()
    for idx, prio in enumerate(priorities):
        wait.append((idx, prio))
        priolist.append((idx, prio))
    priolist = sorted(priolist, key=lambda x: x[1])
    while len(wait) != 0:
        first = wait.popleft()
        if first[1] == priolist[-1][1]:
            priolist.pop()
            answer += 1
            if first[0] == location:
                return answer
        else:
            wait.append(first)
    return answer


def solution(priorities, location):
    queue = [(i, p) for i, p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(
            cur[1] < q[1] for q in queue
        ):  # any -> Return True if bool(x) is True for any x in the iterable. If the iterable is empty, return False.
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer
