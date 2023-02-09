let fs = require('fs');
const filePath = process.platform === `linux` ? `/dev/stdin` : `예제.txt`; 
let input = fs.readFileSync(filePath).toString().split(' ');
const c = console.log

n = Number(input[0])

let dp = []

dp[0] = 0
dp[1] = 1
dp[2] = 1
dp[3] = 2

for(let i = 4 ; i < 41 ; i++){
    dp[i] = dp[i-1] + dp [i-2]
}

let code1 = dp[n]

let code2 = n-2

c(`${code1} ${code2}`)
