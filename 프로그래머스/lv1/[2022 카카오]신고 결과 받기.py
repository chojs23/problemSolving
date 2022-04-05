from collections import defaultdict


def solution(id_list, report, k):
    answer = [0] * len(id_list)
    howMany = defaultdict(set)
    idx = {}
    i = 0
    for id in id_list:
        idx[id] = i
        i += 1
    for r in report:
        f, t = r.split(" ")
        howMany[t].add(f)

    for h in howMany:
        if len(howMany[h]) >= k:
            for name in howMany[h]:
                answer[idx[name]] += 1

    return answer
