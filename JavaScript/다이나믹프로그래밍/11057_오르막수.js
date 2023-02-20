let fs = require('fs');
const filePath = process.platform === `linux` ? `/dev/stdin` : `예제.txt`; 
let input = fs.readFileSync(filePath).toString().split(' ');
const c = console.log

n=Number(input[0])

let d = []

for(let i = 0 ; i < n+1 ; i++){
    d[i] = []
    for(let j = 0 ; j < 9 ; j++){
        d[i][j] = 0
    }
}


for(let i = 0 ; i < 10 ; i++){
    d[1][i] = 1
}
for(let i = 2 ; i < n+1 ; i++){
    for(let j = 9 ; j >= 0 ; j--){
        if (j == 9) {
            d[i][j] = 1
        }
        else {
            d[i][j] = ((d[i-1][j]) + (d[i][j+1]))%10007
        }
    }
}

add = (dp) =>{
    return dp.reduce((a,b) => a+b,0)
}

c(add(d[n])%10007)