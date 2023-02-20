let fs = require('fs');
const filePath = process.platform === `linux` ? `/dev/stdin` : `예제.txt`; 
let input = fs.readFileSync(filePath).toString().split('\n');
const c = console.log

let inputs = input[0].split(' ').map(Number)
n = inputs[0]
m = inputs[1]

let dp = []

for(let i = 0 ; i < 10000+1 ; i++){
    dp[i] = 0
}

dp[0] = 1

for(let i = 1 ; i < n+1 ; i++){
    let a = input[i].split('\n').map(Number)
    for(j = a ; j < m+1 ; j++){
        if(j-a >= 0){
            dp[j] = dp[j]+dp[j-a]
        }
    }
}


c(dp[m])

