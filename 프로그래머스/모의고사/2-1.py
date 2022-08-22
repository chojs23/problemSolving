

# 학생 3명이 가진 수를 다 더했을 때 0 이 되면 삼총사라고 한다. 삼총사 경우의 수 구하기

from itertools import combinations, permutations


def solution(number):
    answer = 0

    for c in combinations(number, 3):
        if sum(c) == 0:
            answer += 1

    # print(answer)
    return answer
