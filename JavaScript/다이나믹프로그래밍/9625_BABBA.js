let fs = require('fs');
const filePath = process.platform === `linux` ? `/dev/stdin` : `예제.txt`; 
let input = fs.readFileSync(filePath).toString().split(' ');
const c = console.log

n = Number(input[0])

let a = []
let b = []

a[0] = 0
a[1] = 1

b[0] = 1
b[1] = 1

for(let i=2 ; i < n+1 ; i++){
    a[i] = b[i-1]
    b[i] = a[i-1] + b[i-1]
}

c(a[n-1] , b[n-1])