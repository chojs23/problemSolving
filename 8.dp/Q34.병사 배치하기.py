n = int(input())

soldier = list(map(int, input().split()))
soldier.reverse()

dp = [1] * n

# LIS (longest increasing subsequence)
# index i가 부분수열의 마지막 원소일 때 dp[i]= i가 마지막인 부분수열의 최대길이
# i 이전까지의 인덱스들 j 중 arr[i]<arr[j]를 만족하는 j의 dp값에 1을 더한다
for i in range(1, n):

    for j in range(i):

        if soldier[j] < soldier[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(dp)
print(n - max(dp))
