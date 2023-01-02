let fs = require('fs');
const filePath = process.platform === `linux` ? `/dev/stdin` : `예제.txt`; 
let input = fs.readFileSync(filePath).toString().split(' ');
const c = console.log

n = Number(input[0])

let dp = []

dp[0] = 0
dp[1] = 1 

for(let i = 2 ; i < 91 ; i++){
    dp[i] = BigInt(dp[i-2]) + BigInt(dp[i-1])
    
}

c(String(dp[n]))