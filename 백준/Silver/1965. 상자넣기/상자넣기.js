let fs = require('fs');
const filePath = process.platform === `linux` ? `/dev/stdin` : `예제.txt`; 
let input = fs.readFileSync(filePath).toString().split('\n');
const c = console.log

n= Number(input[0])

let numbers = input[1].split(" ").map(Number)

let dp = []

for(let i = 0 ; i < n ; i++){
    dp[i] = 1
} 

for(let i = 1 ; i < n ; i++){
    for(let j = 0 ; j < i ; j++){
        if(numbers[i] > numbers[j]){
            dp[i] = Math.max(dp[i],dp[j] +1)
        }

    }
}

c(Math.max(...dp))