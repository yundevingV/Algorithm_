function solution(n) {
    var answer = 0;
    let dp = Array(2001).fill(0)
    dp[0] = 0
    dp[1]=1
    dp[2]=2
    for(let i = 3; i < n+1; i++){
        dp[i] = (dp[i-1] + dp[i-2]) % 1234567
    }
    return dp[n];
}