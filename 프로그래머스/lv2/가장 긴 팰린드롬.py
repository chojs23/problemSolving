def isPalindrome(s):
    if s == s[::-1]:

        return True
    else:
        return False


def solution(s):
    answer = 0
    for checkRange in range(len(s), 1, -1):
        for startIndex in range(len(s)):
            print(checkRange, startIndex, s[startIndex : startIndex + checkRange])

            if isPalindrome(s[startIndex : startIndex + checkRange]):
                answer = max(answer, checkRange)

    return answer
