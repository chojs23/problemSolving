import heapq


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    heap = []
    for idx, food in enumerate(food_times):
        heapq.heappush(heap, (food, idx + 1))
    previous = 0
    sum_value = 0
    length = len(food_times)
    while k - (sum_value + length * (heap[0][0] - previous)) >= 0:
        sum_value += length * (heap[0][0] - previous)
        last = heapq.heappop(heap)
        length -= 1
        previous = last[0]
    result = sorted(heap, key=lambda x: x[1])

    return result[(k - sum_value) % length][1]
