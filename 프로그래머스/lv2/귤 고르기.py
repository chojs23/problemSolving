def solution(k, tangerine):
    answer = 0

    dic = {}

    for t in tangerine:
        dic[t] = dic.get(t, 0) + 1
    dic = sorted(dic.items(), key=lambda x: -x[1])

    for d in dic:
        a, b = d
        k -= b
        answer += 1
        if k <= 0:
            break

    return answer
