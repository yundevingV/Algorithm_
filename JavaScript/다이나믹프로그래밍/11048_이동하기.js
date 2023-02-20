let fs = require('fs');
const filePath = process.platform === `linux` ? `/dev/stdin` : `예제.txt`; 
let input = fs.readFileSync(filePath).toString().split('\n');
const c = console.log

let nm = input[0].split(' ')
let n = Number(nm[0])
let m = Number(nm[1])

let inputsLst = []

for(let i = 1 ; i < n+1 ; i++){
    let inputs = input[i].split(' ').map(Number)
    inputsLst.push(inputs)
}

let dp = []

for(let i = 0 ; i < n+1 ; i++){
    dp[i] = []
    for(let j = 0 ; j < m+1 ; j++){
        dp[i][j] = 0
    }
}

for (let i = 0 ; i < n ; i++){
    for(let j = 0 ; j < m ; j++){
        dp[i+1][j+1] = inputsLst[i][j]
    }
}


for(let i = 1 ; i < n+1 ; i++){
    for(let j = 1 ; j < m+1 ; j++){
        dp[i][j] = Math.max(dp[i-1][j] + dp[i][j], dp[i][j-1]+ dp[i][j])
    }
}

c(dp[n][m])