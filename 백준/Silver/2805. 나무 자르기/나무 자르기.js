const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : '예제.txt';
let input = fs.readFileSync(filePath).toString().trim().split('\n');

const c = console.log;

let numbers = [];

for (let i = 0; i < input.length; i++) {
    if (input[i] === '0 0') {
      end = true;
      break;
    }
    if (input[i] !== '') {
      numbers.push(input[i].split(' '));
    }
  }
//나무의수
let n = numbers[0][0]

// 나무의 길이
let t = numbers[0][1]

let start = 0;
let end = Math.max(...numbers[1]);

const binarySearch = function (m, t) {

    while(start<=end){ 
    
      mid = Math.floor((start + end) / 2);
      let tree = 0;

      for(let i = 0 ; i < m ; i++){
        
        if(numbers[1][i] - mid >= 0) {
          tree += (numbers[1][i] - mid)
          
        } 

      }
      if (tree >= t){
        start = mid + 1}
      else {
        end = mid - 1}
        
      }
    return end;  
    };

c((binarySearch(n,t)));

