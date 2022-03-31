from collections import defaultdict
def solution(n, results):
    answer = 0
    
    winners=defaultdict(set)
    losers=defaultdict(set)
    
    for r in results:
        winners[r[1]].add(r[0])
        losers[r[0]].add(r[1])
    for i in range(1,n+1):
        for winner in winners[i]:
            losers[winner].update(losers[i])
        for loser in losers[i]:
            winners[loser].update(winners[i])
    for i in range(1,n+1):
        if len(winners[i]) + len(losers[i]) == n-1:   # i한테 이기고 진 애들 합쳐서 n-1이면 순위가 결정된 것
            answer += 1        
    
    return answer