def solution(lottos, win_nums):
    match=0
    z_num=lottos.count(0)
    
    for x in lottos:
        if x in win_nums:
            match+=1
    
    
    min=7-match
    if min==7:
        min=6
    max=7-(match+z_num)
    if max==7:
        max=6
    answer = [max,min]
    return answer