from collections import defaultdict
import math


def convert(In, Out):
    h1, m1 = map(int, In.split(":"))
    h2, m2 = map(int, Out.split(":"))
    h = h2 - h1
    if m2 - m1 < 0:
        h -= 1
        m = 60 + m2 - m1
    else:
        m = m2 - m1
    return h * 60 + m


def solution(fees, records):
    answer = []
    bill = defaultdict(int)
    park = defaultdict(list)
    for r in records:
        r = r.split(" ")
        if r[2] == "IN":
            park[r[1]].append(r[0])

        else:
            In = park[r[1]].pop()
            if not park[r[1]]:
                del park[r[1]]
            total = convert(In, r[0])
            bill[r[1]] += total

    for p in park:
        In = park[p].pop()
        total = convert(In, "23:59")
        bill[p] += total

    for i in sorted(bill.keys()):
        fee = fees[1]
        if (bill[i] - fees[0]) > 0:
            fee += math.ceil((bill[i] - fees[0]) / fees[2]) * fees[3]
        answer.append(fee)
    return answer
