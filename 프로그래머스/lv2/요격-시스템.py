# Array, Sorting, Interval
def solution(targets):
    answer = 0
    targets.sort(key=lambda x: x[0])

    for i in range(len(targets) - 1):
        print(targets)
        if targets[i][1] > targets[i + 1][0]:
            targets[i + 1][0] = max(targets[i][0], targets[i + 1][0])
            targets[i + 1][1] = min(targets[i][1], targets[i + 1][1])
        else:
            answer += 1

    answer += 1
    return answer
