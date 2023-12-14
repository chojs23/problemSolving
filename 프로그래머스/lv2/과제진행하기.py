from collections import deque


def solution(plans):
    answer = []

    plans = list(map(lambda x: [x[0], time_to_int(x[1]), int(x[2])], plans))
    sorted_plans = sorted(plans, key=lambda x: x[1])
    index = 1

    q = deque()

    q.append(sorted_plans[0])

    while q:
        print(q)
        subject, start_time, remain_time = q.popleft()

        if (
            index < len(sorted_plans)
            and start_time + remain_time == sorted_plans[index][1]
        ):
            answer.append(subject)
            q.appendleft(
                [
                    sorted_plans[index][0],
                    sorted_plans[index][1],
                    sorted_plans[index][2],
                ]
            )
            index += 1
            continue

        if (
            index < len(sorted_plans)
            and start_time + remain_time < sorted_plans[index][1]
        ):
            answer.append(subject)
            if not q:
                q.appendleft(
                    [
                        sorted_plans[index][0],
                        sorted_plans[index][1],
                        sorted_plans[index][2],
                    ]
                )
                index += 1
            continue

        if (
            index < len(sorted_plans)
            and start_time + remain_time > sorted_plans[index][1]
        ):
            q.appendleft(
                [
                    subject,
                    start_time + remain_time - (sorted_plans[index][1] - start_time),
                    remain_time - (sorted_plans[index][1] - start_time),
                ]
            )
            q.appendleft(
                [
                    sorted_plans[index][0],
                    sorted_plans[index][1],
                    sorted_plans[index][2],
                ]
            )
            index += 1
            continue

        answer.append(subject)

    return answer


def time_to_int(time):
    hour, minute = time.split(":")
    return int(hour) * 60 + int(minute)


solution(
    [["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]
)
