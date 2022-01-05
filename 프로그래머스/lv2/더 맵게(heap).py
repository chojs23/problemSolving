import heapq


def solution(scoville, k):
    answer = 0
    heapq.heapify(scoville)

    while scoville[0] <= k:
        if len(scoville) < 2:
            return -1
        answer += 1
        new = heapq.heappop(scoville) + heapq.heappop(scoville) * 2
        heapq.heappush(scoville, new)

    return answer
