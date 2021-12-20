import itertools


def solution(numbers):
    answer = []

    comb = itertools.combinations(numbers, 2)

    for i in comb:
        a = sum(i)
        if a not in answer:
            answer.append(a)
    answer.sort()
    return answer
