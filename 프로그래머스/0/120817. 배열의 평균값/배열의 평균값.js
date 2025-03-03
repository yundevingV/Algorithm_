function solution(numbers) {
    var answer = 0;
    const len = numbers.length;
    const sum = numbers.reduce((acc,cur) => acc + cur, 0);
    return sum / len;
}