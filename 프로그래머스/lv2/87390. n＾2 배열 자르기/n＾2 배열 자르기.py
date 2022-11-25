def solution(n, left, right):
    answer = []
    for i in range(left,right+1):
        a = i//n
        b = i%n 
        a=max(a,b)
        answer.append(a+1)
    
    return answer