# Heap
import heapq


def solution(numbers):
    n = len(numbers)
    answer = [-1] * n
    h = []

    for i in range(n):
        value = numbers[i]

        while h and h[0][0] < value:
            _, idx = heapq.heappop(h)
            answer[idx] = value

        heapq.heappush(h, (value, i))
    return answer
