import math


def convert(n, base):  # n진법 변환
    arr = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return arr[r]
    else:
        return convert(q, base) + arr[r]


def isprime(n):

    if n == 0 or n == 1:
        return False
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True


def getNumberArray(n):
    return map(int, filter(lambda x: x != "", n.split("0")))


def solution(n, k):
    answer = 0
    string = convert(n, k)
    nums = getNumberArray(string)

    for num in nums:
        # print(num)
        if isprime(num):
            answer += 1

    return answer
