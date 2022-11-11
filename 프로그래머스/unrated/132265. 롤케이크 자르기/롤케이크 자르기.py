from collections import defaultdict
def solution(topping):
    answer = 0

    dic = {}
    dic.get
    for t in topping:
        dic[t] = dic.get(t, 0) + 1
    countA = defaultdict(int)
    haveA = 0
    haveB = len(set(topping))
    for i in range(len(topping)):
        a = topping[i]

        if countA[a] == 0:
            haveA += 1
            countA[a] += 1
        else:
            countA[a] += 1

        if dic[a] == 1:
            haveB -= 1
            dic[a] -= 1
        elif dic[a] > 1:
            dic[a] -= 1
        else:
            print("adssa")

        if haveA == haveB:
            answer += 1

    print(answer)
    return answer