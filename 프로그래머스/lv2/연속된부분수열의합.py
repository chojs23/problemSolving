def solution(sequence, k):
    n = len(sequence)

    max_sum = 0
    end = 0

    res = []
    for i in range(n):
        while max_sum < k and end < n:
            max_sum += sequence[end]
            end += 1

        if max_sum == k:
            res.append([i, end - 1, end - 1 - i])

        max_sum -= sequence[i]

    res = sorted(res, key=lambda x: x[2])
    return res[0][:2]
