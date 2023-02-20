let fs = require('fs');
const filePath = process.platform === `linux` ? `/dev/stdin` : `예제.txt`; 
let input = fs.readFileSync(filePath).toString().split('\n');
const c = console.log

n = Number(input[0])
let lst= []
lst.push(0)


let numbers = input[1].split(" ").map(Number)

lst = lst.concat(numbers)


let dp = []

for(let i = 0 ; i < n+1 ; i++){
    dp[i] = 0
}



for(let i = 1 ; i < n+1 ; i++){
    for(let j = 1 ; j < i+1 ; j++){
        dp[i] = Math.max(dp[i-j] + lst[j] , dp[i])
    }
}


c(dp[n])
