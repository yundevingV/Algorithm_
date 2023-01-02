let fs = require('fs');
const filePath = process.platform === "linux" ? "/dev/stdin" : "예제.txt";
let input = fs.readFileSync(filePath).toString().split('\n');
const c = console.log


let count = Number(input[0]);

let numbers = [];

//입력값 받기
for (let i = 1; i < input.length; i++) {
    if (input[i] !== '') {
        numbers.push(input[i].split(' '));
    }
}
//dp테이블 생성
let dp = []

for (let i=0;i<31;i++){
    dp[i] = []
    for (let j = 0;j<31;j++){
        dp[i][j] = 0
    }
}

for (let i = 1 ; i < 31 ; i++) {
    for (let j = 1 ; j < 31 ;j++) {
    
        if (j === '1') {
            dp[i][1] = i
        } 
        else if (i === j) {
            dp[i][i] = 1
        }
        else if (j === '0') {
            dp[i][0] = 1
        } 
        else {
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        }
    }
}

for (let i=0 ; i < numbers.length ; i++) {
    console.log(dp[Number(numbers[i][1])+1][Number(numbers[i][0])+1])
}

console.log(dp)