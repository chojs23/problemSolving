def solution(m, n, puddles):
    answer = 0
    m,n=n,m
    #dp[i][j]=dp[i-1][j]+dp[i][j-1]
    dp=[[0 for _ in range(n)] for _ in range(m)]
    dp[0]=[1]*n
    
    for i in range(m):
        dp[i][0]=1
    
    
    for p in puddles:
        if p[0]-1==0:
            for i in range(m-(p[1]-1)):
                dp[i+p[1]-1][0]=0
        if p[1]-1==0:
            for i in range(n-(p[0]-1)):
                dp[0][i+p[0]-1]=0
        dp[p[1]-1][p[0]-1]=0
    
    
    #print(dp)    
    for i in range(1,m):
        for j in range(1,n):
            if [j+1,i+1] not in puddles:
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
    
    #print(dp)
    
    
    return dp[m-1][n-1]%1000000007