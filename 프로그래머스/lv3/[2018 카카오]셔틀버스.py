def solution(n, t, m, timetable):
    answer = ""

    timetable = [int(time[:2]) * 60 + int(time[3:]) for time in timetable]
    timetable.sort()

    busTime = [9 * 60 + t * i for i in range(n)]

    i = 0  # 버스에 탈 크루의 인덱스
    for bt in busTime:  # 버스 도착 시간을 순회하면서
        cnt = 0  # 버스에 타는 크루 수
        while cnt < m and i < len(timetable) and timetable[i] <= bt:
            i += 1
            cnt += 1
        if cnt < m:  # 버스에 자리 남았으면 버스타임에 내가 타면 됨
            answer = bt
        else:  # 버스에 탈 자리 없으면 맨 마지막 크루보다 1분전에 도착
            answer = timetable[i - 1] - 1
    answer = str(answer // 60).zfill(2) + ":" + str(answer % 60).zfill(2)
    return answer
