let fs = require('fs');
const filePath = process.platform === `linux` ? `/dev/stdin` : `예제.txt`; 
let input = fs.readFileSync(filePath).toString().split('\n');
const c = console.log
let lst = []

for (let i = 1 ; i <= input[0] ; i++){
    let numbers = input[i].split(" ").map(Number)
    lst.push(numbers)
}

lst.sort((a,b) => a[0] - b[0])

let dp = []

for(let i = 0 ; i < Number(input[0]) ; i++){
    dp[i] = 1
}

for(let i = 1 ; i < Number(input[0]) ; i++){
    for(let j = 0; j < i ; j++){
        if(lst[j][1] < lst[i][1]){
            dp[i] = Math.max(dp[i],dp[j]+1)
        }
    }
}

c(Number(input[0]) - Math.max(...dp))