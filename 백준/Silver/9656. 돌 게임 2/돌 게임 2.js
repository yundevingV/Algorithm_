let fs = require('fs');
const filePath = process.platform === `linux` ? `/dev/stdin` : `예제.txt`; 
let input = fs.readFileSync(filePath).toString().split(' ');
const c = console.log

n = Number(input[0])

let dp = []

for (let i = 0 ; i < n+1 ; i++){
    if (i % 2 == 0){
        dp[i] = 1
    }
    else {
        dp[i] = 0
    }
}

if (dp[n] == 1){
    c('SK')
}
else {
    c('CY')
}

