let fs = require('fs');
const filePath = process.platform === `linux` ? `/dev/stdin` : `예제.txt`; 
let input = fs.readFileSync(filePath).toString().split('\n');
const c = console.log

let list1 = (input[0].split(' ').map(Number))

let p = list1[1]

let list2 = (input[1].split(' ').map(Number))

let result = list2.filter(i => i < p)

c(result.join(' '))