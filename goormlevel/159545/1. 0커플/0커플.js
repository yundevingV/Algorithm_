const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let n = 0;
let numbers = [];

rl.on('line', (line) => {
    if (n === 0) {
        // 첫 번째 줄 입력 처리: 사람 수 n
        n = parseInt(line);
    } else {
        // 두 번째 줄 이후 입력 처리: n 개의 숫자
        numbers = line.split(' ').map(num => parseInt(num));

        // 입력이 완료되었으므로 문제 해결 함수 호출
        let result = solution(numbers);
        console.log(result);

        // 입력이 완료되었으므로 프로그램 종료
        rl.close();
    }
});

function solution(numbers) {
    let numMap = new Map();
    let unmatchedSum = 0;

    for (let num of numbers) {
        if (numMap.has(num)) {
            let count = numMap.get(num);
            if (num === 0 && count > 0) {
                unmatchedSum -= num; // 쌍을 찾은 것으로 처리
                numMap.set(num, count - 1);
            } else {
                let opposite = -num;
                if (numMap.has(opposite) && numMap.get(opposite) > 0) {
                    unmatchedSum -= num; // 쌍을 찾은 것으로 처리
                    numMap.set(opposite, numMap.get(opposite) - 1);
                } else {
                    numMap.set(num, count + 1);
                }
            }
        } else {
            numMap.set(num, 1);
        }
    }

    numMap.forEach((count, num) => {
        if (count > 0) {
            unmatchedSum += num * count;
        }
    });

    return unmatchedSum;
}