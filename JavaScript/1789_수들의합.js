let fs = require('fs');
const filePath = process.platform === `linux` ? `/dev/stdin` : `예제.txt`; 
let input = fs.readFileSync(filePath).toString()
const c = console.log

let n = Number(input)

let temp = 0 
let count = 0

for(let i = 1 ;; i++){
    temp += i
    count +=1
    if (temp > input){
        count-=1
        break
    }

}

c(count)