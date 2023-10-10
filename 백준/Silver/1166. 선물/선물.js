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

let n = numbers[0][0];
let l = numbers[0][1];
let w = numbers[0][2];
let h = numbers[0][3];

s = 0;
e = Math.max(l,w,h);

for(let i = 0 ; i < 1000 ; i ++){
  m = (s+e) / 2
  if(Math.floor(l/m) * Math.floor(w/m) * Math.floor(h/m) < n) {e = m}
  else {s = m}
}

c(e.toFixed(10))