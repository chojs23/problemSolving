def solution(n, arr1, arr2):
    answer = []

    for i, j in zip(arr1, arr2):
        c = bin(i | j)

        a = c.replace("0b", "").zfill(n).replace("1", "#").replace("0", " ")

        answer.append(a)

    return answer
