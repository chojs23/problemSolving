from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    for c in course:
        temp = []
        for order in orders:
            combi = combinations(sorted(order), c)
            temp += combi
        counter = Counter(temp)
        # print(counter)
        answer += [
            "".join(f)
            for f in counter.keys()
            if counter[f] == max(counter.values()) and counter[f] >= 2
        ]

    return sorted(answer)
