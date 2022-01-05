import math
def solution(w,h):
    gcd=math.gcd(w,h)
    answer=w*h-(w//gcd+h//gcd-1)*gcd
    return answer