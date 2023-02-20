let fs = require('fs');
const filePath = process.platform === `linux` ? `/dev/stdin` : `예제.txt`; 
let input = fs.readFileSync(filePath).toString().trim().split('');
const c = console.log

str=''

for(let i = input.length-1; i >= 0 ; i--){
    str = input[i].concat(str)
}

ans = Number(str)

let dp = []
dp[0]=0

let p = 1
let pivot = 1
let pivot2 = 1


for (let i = 1 ; i < 501 ; i++) {

    if (pivot % 25 === 0){
        p+=5
        
    }
    if (pivot2 % 125 === 0) {
        p+=5
        
    }

    dp[i] = parseInt(p/5)
    
    p+=1
    pivot+=1
    pivot2+=1
}

c(dp[ans])