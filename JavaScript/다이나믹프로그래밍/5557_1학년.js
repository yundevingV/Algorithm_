let fs = require('fs');
const filePath = process.platform === `linux` ? `/dev/stdin` : `예제.txt`; 
let input = fs.readFileSync(filePath).toString().split('\n');
const c = console.log

n = Number(input[0])

let lst = input[1].split(' ').map(Number)

let dp = []

for(let i = 0 ; i < n+1 ; i++){
    dp[i] = []
    for(let j = 0 ; j < 21 ; j++){
        dp[i][j] = BigInt(0)
    }
}

for(i in lst){
    if (i == 0){
        dp[i][lst[0]] = BigInt(1)    
        continue
    }
    for (let j = 0 ; j < 21 ; j++){
        next = dp[i-1][j]
        if (next){
            if (j + lst[i] <= 20){
                dp[i][j+lst[i]] += BigInt(next)
            }
            if (j - lst[i] >= 0){
                dp[i][j-lst[i]] += BigInt(next)
            }
        }
    }
}

c(dp[n-2][[lst[n-1]]].toString())