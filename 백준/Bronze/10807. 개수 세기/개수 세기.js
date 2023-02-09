let fs = require('fs');
const filePath = process.platform === `linux` ? `/dev/stdin` : `예제.txt`; 
let input = fs.readFileSync(filePath).toString().split('\n');
const c = console.log

let n = Number(input[0])

let lst = (input[1].split(' ').map(Number))

let answer = Number(input[2])

let count = lst.length

for(let i = 0 ; i < n ; i++){
    
    if (answer != lst[i]) {
        count -=1
    }
}

c(count)