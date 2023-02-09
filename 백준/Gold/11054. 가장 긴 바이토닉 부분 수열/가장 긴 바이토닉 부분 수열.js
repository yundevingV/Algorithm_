const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");

const n = +input[0];
const nums = input[1].split(" ").map(Number);

const increaseDP = new Array(n).fill(1);
const decreaseDP = new Array(n).fill(1);

// 증가 DP 구하기
for (let i = 0; i < n; i++) {
  const cur = nums[i];
  let cnt = 1;
  for (let j = 0; j < i; j++) {
    const compare = nums[j];
    if (cur > compare) cnt = Math.max(cnt, increaseDP[j] + 1);
  }
  increaseDP[i] = cnt;
}

// 감소 DP 구하기
for (let i = n - 1; i >= 0; i--) {
  const cur = nums[i];
  let cnt = 1;
  for (let j = i + 1; j < n; j++) {
    const compare = nums[j];
    if (cur > compare) cnt = Math.max(cnt, decreaseDP[j] + 1);
  }
  decreaseDP[i] = cnt;
}

console.log(
  Math.max(...increaseDP.map((incVal, index) => incVal + decreaseDP[index])) - 1
);