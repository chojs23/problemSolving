from collections import deque


def check(s, begin):
    answer = 0
    for i in range(len(s)):
        if list(s)[i] != list(begin)[i]:
            answer += 1
    return True if answer == 1 else False


def solution(begin, target, words):
    if target not in words:
        return 0
    res = 0
    q = deque()
    q.append(begin)
    visited = [0] * len(words)
    a = {}

    while q:
        res += 1
        for i in range(len(q)):
            now = q.popleft()
            if now == target:
                return res - 1
            for j in range(len(words)):
                if check(words[j], now) and visited[j] == False:
                    visited[j] = True
                    q.append(words[j])
