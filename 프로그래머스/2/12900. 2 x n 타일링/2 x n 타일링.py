def solution(n):
    answer = 0
    dp = [1,2]
    
    
    for i in range(2,n+1) :
        dp.append((dp[i-1] + dp[i-2])% 1000000007)
    return dp[n-1]