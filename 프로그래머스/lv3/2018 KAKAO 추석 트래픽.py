def solution(lines):
    answer = 0
    start_time = []
    end_time = []

    for t in lines:
        time = t.split(" ")
        start_time.append(get_start_time(time[1], time[2]))
        end_time.append(get_time(time[1]))
    # print(start_time,end_time)
    for i in range(len(lines)):
        cnt = 0
        cur_end_time = end_time[i]
        # i번째는 현재 자신의 시작시간이고, i 이하는 그 이전의 시작시간이므로 카운트 할 필요가 없다.
        for j in range(i, len(lines)):
            if cur_end_time + 1000 > start_time[j]:
                cnt += 1
        answer = max(answer, cnt)
    return answer


def get_time(time):
    hour = int(time[:2]) * 3600
    minute = int(time[3:5]) * 60
    second = int(time[6:8])
    millisecond = int(time[9:])
    return (hour + minute + second) * 1000 + millisecond


def get_start_time(time, duration):
    n_time = duration[:-1]
    int_duration_time = int(float(n_time) * 1000)
    return get_time(time) - int_duration_time + 1
