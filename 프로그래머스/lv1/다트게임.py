def solution(dartResult):
    answer = 0
    score = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A"]
    bonus = ["S", "D", "T"]
    op = ["*", "#"]
    result = []
    dartResult = dartResult.replace("10", "A")
    for i in dartResult:
        if i in score:
            if i == "A":
                result.append(10)
            else:
                result.append(int(i))
            print(result)
        elif i in bonus:
            if i == "S":
                result[-1] = result[-1] ** 1
            elif i == "D":
                result[-1] = result[-1] ** 2
            else:
                result[-1] = result[-1] ** 3
        else:
            if i == "*":
                if len(result) > 1:
                    result[-2] *= 2
                    result[-1] *= 2
                else:
                    result[-1] *= 2
            else:

                result[-1] *= -1
    print(result)
    answer = sum(result)
    return answer
