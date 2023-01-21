const fs = require('fs');
let input = fs.readFileSync("/dev/stdin").toString();
let sum = 0, cnt = 0;

for(let i =1;; i++){
    sum += i
    cnt+=1;
    if(sum > input){
        cnt-=1;
        break;
    }
}

console.log(cnt);