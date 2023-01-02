let fs = require('fs');
const filePath = process.platform === `linux` ? `/dev/stdin` : `예제.txt`; 
let input = fs.readFileSync(filePath).toString().split('\n');
const c = console.log
let lst = []


for (let i = 1 ; i <= input[0] ; i++){
    let numbers = input[i].split(" ").map(Number)
    lst.push(numbers)
}

c(lst)

let dp = []

