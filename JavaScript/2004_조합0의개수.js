let fs = require('fs');
const filePath = process.platform === `linux` ? `/dev/stdin` : `예제.txt`; 
let input = fs.readFileSync(filePath).toString().trim().split(' ');
const c = console.log

let lst = []

for (v of input){
    lst.push(Number(v))
}

k = lst[0]
n = lst[1]
kn = k-n

mod5 = (num) => {
    count = 0
    while (num >= 5){
        count += parseInt(num/5)
        num = parseInt(num)/5
    }
    return count
}

mod2 = (num) => {
    count = 0
    while (num >= 2){
        count += parseInt(num/2)
        num = parseInt(num)/2
    }
    return count
}

countTwo = mod2(k) - (mod2(n) + mod2(kn))
countFive = mod5(k) - (mod5(n) + mod5(kn))

if (countTwo >= countFive){
    sub = countTwo - countFive
    c(countTwo - sub)
} 
else {
    sub = countFive - countTwo
    c(countFive - sub)
}