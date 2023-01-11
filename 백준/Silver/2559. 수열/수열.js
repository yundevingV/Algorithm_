let fs = require('fs');
const filePath = process.platform === `linux` ? `/dev/stdin` : `예제.txt`; 
let input = fs.readFileSync(filePath).toString().split('\n');
const c = console.log

let inputs = input[0].split(' ').map(Number)
n = inputs[0]
m = inputs[1]

let lst = input[1].split(' ').map(Number)

let prefix_sum = [0]


let temp = 0 
for(let i = 0 ; i < n ; i++){
    
    temp += lst[i]
    prefix_sum.push(temp)
    temp = prefix_sum[i+1] 
}

let maxNum = -10000001

for(let i = m ; i < n+1 ; i++){
    maxNum = Math.max(maxNum , prefix_sum[i] - prefix_sum[i-m])
}

c(maxNum)