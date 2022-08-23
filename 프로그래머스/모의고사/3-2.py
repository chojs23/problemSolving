

def solution(ingredient):
    answer = 0

    stk = []
    # 빵 야채 고기 빵
    # 1 2 3
    for i in ingredient:
        stk.append(i)

        if len(stk) >= 4 and stk[-4:] == [1, 2, 3, 1]:
            answer += 1
            stk.pop()
            stk.pop()
            stk.pop()
            stk.pop()
    print(answer)
    return answer


solution([2, 1, 1, 2, 3, 1, 2, 3, 1])
