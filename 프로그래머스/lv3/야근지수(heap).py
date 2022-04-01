import heapq


def solution(n, works):
    answer = 0
    for i in range(len(works)):
        works[i] *= -1
    heapq.heapify(works)

    for i in range(n):
        num = heapq.heappop(works)
        num += 1
        heapq.heappush(works, num)

    if works[0] >= 0:
        return 0
    for w in works:
        answer += w**2
    return answer
