let fs = require('fs'); 
const filePath = process.platform === `linux` ? `/dev/stdin` : `예제.txt`; 
let input = fs.readFileSync(filePath).toString().split(' ');
const c = console.log

n = Number(input[0])


let dp = []

for(let i = 0 ; i < n+1 ; i++){
    dp[i] = []
    for(let j = 0 ; j < 10 ; j++){
        dp[i][j] = 0
    }
}

for(let i = 1 ; i<10 ; i++){
    dp[1][i] = 1
}

for (let i = 2 ; i < n+1 ; i++){
    for (let j = 0 ; j < 10 ; j++){

        if (j === 0){
            dp[i][j] = (dp[i-1][1]) % 1000000000
        } 
        else if (j === 9) {
            dp[i][j] = dp[i-1][8] % 1000000000
        }
        else {
            dp[i][j] = ((dp[i-1][j+1]) + (dp[i-1][j-1])) % 1000000000
        }
    }
}

add = (dp) =>{
    return dp.reduce((a,b) => a+b,0)
}

c((add(dp[n]) % 1000000000))
