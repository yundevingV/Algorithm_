let fs = require('fs');
const filePath = process.platform === `linux` ? `/dev/stdin` : `예제.txt`; 
let input = fs.readFileSync(filePath).toString().split(' ');
const c = console.log

let n = (Number(input[0]))

let dp = []
dp[1] = 0
dp[2] = 1

for(let i = 3 ; i < 11 ; i++){
    dp[i] = i-1 + dp[i-1]
}

c(dp[n])