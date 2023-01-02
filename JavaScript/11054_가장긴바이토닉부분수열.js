let fs = require('fs');
const filePath = process.platform === `linux` ? `/dev/stdin` : `예제.txt`; 
let input = fs.readFileSync(filePath).toString().split('\n');
const c = console.log

n = Number(input[0])

let numbers = input[1].split(" ").map(Number)

let dp = []
let dp2 = []

for (let i = 0 ; i < n ; i++){
    dp[i] = 1
    dp2[i] = 1
}

for (let i = 1 ; i < n ; i++){
    for (let j=0 ; j < i ; j++){
        if (numbers[i] > numbers[j]){
            dp[i] = Math.max(dp[i] , dp[j]+1)
        }
    }
}

for (let i = n-1 ; i >= 0 ; i--){
    for (let j = i+1 ; j < n ; j++){
        if (numbers[i] > numbers[j]){
            dp2[i] = Math.max(dp2[i] , dp2[j]+1)            
        }
        
    }
}

let result = []

for (let i = 0 ; i < dp.length ; i++){
    result[i] = dp[i]+dp2[i]-1
}

c(Math.max(...dp.map((incVal, index) => incVal + dp2[index])) - 1);