import heapq


def solution(program):
    answer = [0] * 11

    program.sort(key=lambda x: x[1])
    heap = []

    index = 0
    cnt = 0
    total_time = 0

    while cnt < len(program):
        while index < len(program) and program[index][1] <= total_time:
            heapq.heappush(heap, program[index])
            index += 1
        if heap:
            p = heapq.heappop(heap)
            answer[p[0]] += total_time - p[1]
            total_time += p[2]
            cnt += 1
        else:
            total_time = program[index][1]

    answer[0] = total_time

    return answer
