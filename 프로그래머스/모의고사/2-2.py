

def solution(topping):
    answer = 0

    L, R = dict(), dict()

    for num in topping:
        if num not in R:
            R[num] = 1
        else:
            R[num] += 1

    for num in topping:
        R[num] -= 1
        if R[num] == 0:
            del R[num]
        if num not in L:
            L[num] = 1
        else:
            L[num] += 1

        if len(L.keys()) == len(R.keys()):
            answer += 1

    return answer


solution([1, 2, 1, 3, 1, 4, 1, 2])
solution([1, 2, 3, 1, 4])
