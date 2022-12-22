import sys

n,m = map(int , sys.stdin.readline().split())

dp = [[0 for i in range(n+1)] for i in range(n+1)]

for i in range(n+1) :
    for j in range(n+1) :
        # 3C1 처리
        if j == 1 :
            dp[i][j] = i
        # 3C3 처리
        elif i == j :
            dp[i][j] = 1
        #3C0 처리
        elif j == 0 :
            dp[i][j] = 1
        else :
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

print(dp[n][m])