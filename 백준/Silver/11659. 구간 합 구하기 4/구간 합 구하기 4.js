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

for (i of lst){
    temp +=i
    prefix_sum.push(temp)
}

let result = []

for(let i = 2 ; i < m+2 ; i++){
    let x = input[i].split(' ').map(Number)
    start = x[0]
    end = x[1]

    result.push(prefix_sum[end] - prefix_sum[start-1] )

}

c(result.join('\n'))
