from collections import deque


def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    i = 0

    while i < len(cities):

        cur = cities[i].lower()

        if cur in cache:
            answer += 1
            cache.remove(cur)
            cache.append(cur)
        else:
            answer += 5
            cache.append(cur)

        if len(cache) > cacheSize:
            cache.popleft()
        i += 1

    return answer
