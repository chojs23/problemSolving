# Stack
def solution(orders):
    answer = 0
    additional_container = []
    current = 1

    idx = 0

    while current <= len(orders) or len(additional_container) > 0:
        if orders[idx] == current:
            current += 1
            idx += 1
            answer += 1
        else:
            if (
                len(additional_container) > 0
                and additional_container[-1] == orders[idx]
            ):
                additional_container.pop()
                answer += 1
                idx += 1
            else:
                additional_container.append(current)
                current += 1

        if current > len(orders) and len(additional_container) > 0:
            if additional_container[-1] == orders[idx]:
                additional_container.pop()
                answer += 1
                idx += 1
            else:
                break

    return answer


# test
print(solution([4, 3, 1, 2, 5]))
print(solution([5, 4, 3, 2, 1]))


# [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15] stack
#
# [] truck
#
# [] stack
