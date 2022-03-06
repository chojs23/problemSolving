def solution(n, times):
    answer = 0
    times.sort()

    # 이진탐색을 위한 최솟값과 최댓값 설정
    # 이진탐색할 대상은 시간
    l = 1
    r = times[0] * n

    while l <= r:
        # cnt = mid시간 동안 심사가능한 사람
        m = (l + r) // 2
        cnt = 0
        for time in times:
            cnt += m // time
            if cnt >= n:
                break
        if cnt >= n:
            answer = m
            r = m - 1
        else:
            l = m + 1
    return answer
