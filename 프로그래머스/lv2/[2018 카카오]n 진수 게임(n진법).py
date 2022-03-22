def convert(n, base):  # n진법 변환
    arr = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return arr[r]
    else:
        return convert(q, base) + arr[r]


def solution(n, t, m, p):
    answer = ""
    test = ""
    for i in range(m * t):
        test += str(convert(i, n))
    # print(test)
    while len(answer) < t:
        answer += test[p - 1]
        p += m

    return answer
