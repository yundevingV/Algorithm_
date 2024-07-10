function solution(numbers, k) {
    let stack = [];
    let count = k; // 제거해야 할 숫자의 개수

    for (let num of numbers) {
        // stack의 마지막 숫자와 비교하여 현재 숫자가 더 크면 stack에서 pop
        while (count > 0 && stack.length > 0 && stack[stack.length - 1] < num) {
            stack.pop();
            count--;
        }
        stack.push(num);
    }

    // 남은 숫자 중에서 k개를 제거하지 못한 경우
    stack.splice(stack.length - count, count);

    // 배열을 문자열로 변환하여 반환
    return stack.join('');
}