import itertools
import math


def solution(n, weak, dist):
    answer = math.inf
    weakSize = len(weak)
    weak = weak + [w + n for w in weak]
    for start in range(weakSize):
        for d in itertools.permutations(dist, len(dist)):
            cnt = 1
            pos = start
            for i in range(1, weakSize):
                nextPos = start + i
                diff = weak[nextPos] - weak[pos]
                if diff > d[cnt - 1]:
                    pos = nextPos
                    cnt += 1
                    if cnt > len(dist):
                        break
            if cnt <= len(dist):
                answer = min(answer, cnt)

    return answer if answer != math.inf else -1
