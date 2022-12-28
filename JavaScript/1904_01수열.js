let fs = require('fs');
const filePath = process.platform === "linux" ? `/dev/stdin` : `예제.txt`; 
let input = fs.readFileSync(filePath).toString().trim().split(' ');
const c = console.log

n = Number(input[0])

let dp = []

dp[1] = 1 
dp[2] = 2
dp[3] = 3

for(let i = 4 ; i < 1000001 ; i++){
    dp[i] = (dp[i-2] ) + (dp[i-1] )
    if (dp[i] >= 15746) {
        dp[i] = Number(dp[i]%15746)
    }
}

c(dp[n])