def solution(N, stages):

    success = {x: 0 for x in stages}
    for i in stages:
        success[i] += 1
    success = dict(sorted(success.items()))
    print(success)

    length = len(stages)
    temp = 0
    fail = {x: 0 for x in range(1, N + 1)}

    for i in range(1, N + 1):
        if i in success:
            fail[i] = success[i] / (length - temp)
            temp += success[i]

    return sorted(fail, key=lambda x: fail[x], reverse=True)
