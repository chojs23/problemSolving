# Implementation, Product
from itertools import product


def solution(users, emoticons):
    discount_rates = [10, 20, 30, 40]
    result = []

    discount_cases = list(product(discount_rates, repeat=len(emoticons)))

    for discount_case in discount_cases:
        members = 0
        income = 0

        for required_discount, budget in users:
            purchased = 0
            for i in range(len(emoticons)):
                if required_discount <= discount_case[i]:
                    purchased += emoticons[i] - emoticons[i] * discount_case[i] * 0.01
            if purchased >= budget:
                members += 1
            else:
                income += purchased
        result.append((members, income))
    answer = sorted(result, reverse=True, key=lambda x: (x[0], x[1]))

    return answer[0]
