answer = 0


def dfs(numbers, target, idx, result):

    global answer
    if idx == len(numbers):
        if result == target:
            answer += 1
        return
    else:
        dfs(numbers, target, idx + 1, result + numbers[idx])
        dfs(numbers, target, idx + 1, result - numbers[idx])


def solution(numbers, target):

    dfs(numbers, target, 0, 0)

    return answer
