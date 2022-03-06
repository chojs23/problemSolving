def solution(s):
    answer = 1
    stack = []
    for i in range(len(s)):
        stack.append(s[i])
        if len(stack) > 1 and stack[-2] == stack[-1]:
            stack.pop()
            stack.pop()

    if stack:
        answer = 0

    return answer
