def solution(progresses, speeds):

    day = []
    for i, j in zip(progresses, speeds):
        if len(day) == 0 or day[-1][0] < -((i - 100) // j):
            day.append([-((i - 100) // j), 1])
        else:
            day[-1][1] += 1

    return [d[1] for d in day]
