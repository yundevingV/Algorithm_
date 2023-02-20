let fs = require('fs');
const { join } = require('path');
const filePath = process.platform === "linux" ? "/dev/stdin" : "예제.txt";
let input = fs.readFileSync(filePath).toString().split('\n');
const c = console.log

let inputs = input[0].split(" ").map(Number)

let n = inputs[0]
let weight = inputs[1]

let w = []
let v = []

let dp = []

for(let i = 0 ; i< n+1 ; i++){
    dp[i] = []
    for(let j = 0 ; j < weight +1 ; j++){
        dp[i][j] = 0
    }
}
for(let i = 1 ; i < n+1 ; i++){
    let numbers = (input[i].split(' ').map(Number))
    w.push(numbers[0])
    v.push(numbers[1])
}

for(let i = 1 ; i < n+1 ; i++){
    for(let j = 1 ; j < weight+1 ; j++){
        if (j < w[i-1]){
            dp[i][j] = dp[i-1][j]
        } else {
            dp[i][j] = Math.max(dp[i-1][j] , dp[i-1][j-w[i-1]] + v[i-1])

        }
    
    }
}

c(dp[n][weight])