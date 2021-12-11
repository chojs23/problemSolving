def solution(numbers, hand):
    answer = ''
    l=[1,4,7]
    r=[3,6,9]
    left=10
    right=12
    
    for i in numbers:
        if i ==0 :
            i=11
        if i in l:
            left=i
            answer+="L"
        elif i in r:
            right=i
            answer+="R"
        else:
            ml=abs(i-left)
            mr=abs(i-right)
            
            if ml%3+ml//3 >mr%3+mr//3:
                right=i
                answer+="R"
            elif ml%3+ml//3 <mr%3+mr//3:
                left=i
                answer+="L"
            else:
                if hand=="right":
                    right=i
                    answer+="R"
                else:
                    left=i
                    answer+="L"
    return answer