const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : '예제.txt';
let input = fs.readFileSync(filePath).toString().trim().split('\n');

const c = console.log;

let numbers = [];
let end = false;

for (let i = 0; i < input.length; i++) {
  if (input[i] === '0 0') {
    end = true;
    break;
  }
  if (input[i] !== '') {
    numbers.push(input[i].split(' '));
  }
}

// 돈 -> kw
const convertKw = (m) => {
    let kw = 0 
    if(m <= 200) {
        return Math.floor(m / 2);
    } 
    else if (m <= 29900) {
        return Math.floor((m-200) / 3 + 100)
    } else if (m <= 4979900) {
        return Math.floor((m-29900) / 5 + 10000)
    } else {
        return Math.floor((m-4979900) / 7 + 1000000)
    }
}

// kw -> 돈
const convertM = (kw) => {
    
    if(kw <= 100) {
        return kw * 2
    } else if (kw <= 10000) {
        return 200 + (kw - 100) * 3
    } else if (kw <= 1000000) {
        return 200 + 29700 + (kw - 10000) * 5
    } else {
        return 200 + 29700 + 4950000 + (kw - 1000000) * 7
    }
}

const binarySearch = function (m, target) {
    // TODO : 여기에 코드를 작성합니다.
    let total = convertKw(m) 
    let start = 0;
    let end = convertKw(m)
    
    while(start<=end){ //점점 좁혀지다가 start와 end의 순서가 어긋나게 되면 반복을 종료한다
    
    let mid = Math.floor((start+end)/2)
    
    let sPrice = Math.floor(convertM(mid));
    let bPrice = Math.floor(convertM(total - mid));

    t = Math.abs(sPrice - bPrice);

    if (t < target){
        end = mid - 1

    } else if (t > target) {
        start = mid + 1

    } else {
        return convertM(mid)
    }
    }

    };


for(let i = 0 ; i < numbers.length ; i++){
    c(binarySearch(numbers[i][0],numbers[i][1]))
}
