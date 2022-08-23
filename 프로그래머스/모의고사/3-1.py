

def solution(a, b, n):
    answer = 0
    cur = n
    while True:
        if n < a:
            break
        give = (n//a)*a
        get = (n//a)*b
        answer += get
        cur = cur-give+get

        n = cur
    print(answer)
    return answer


solution(2, 1, 20)
solution(3, 1, 20)
