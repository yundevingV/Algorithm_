let fs = require('fs');
const { join } = require('path');
const filePath = process.platform === "linux" ? "/dev/stdin" : "예제.txt";
let input = fs.readFileSync(filePath).toString().split('\n');
const c = console.log

let inputs = input[0].split(" ").map(Number)

let n = inputs[0]
let weight = inputs[1]

let lst = []

for(let i = 1 ; i < n+1 ; i++){
    lst.push(input[i].split(" ").map(Number))
}
let dp = []

for(let i = 0 ; i< n ; i++){
    dp.push(lst[i])
}

c(dp)

for(let i = 0 ; i < n ; i++){
    for(let j = 0 ; j < n ; j++){
        
        if (weight > dp[i][0]) {
            c(i,j)
            dp[i][0] += dp[j][0]
            dp[i][1] += dp[j][1]
        } 
    }
}

c(dp)