function solution(numbers, target) {
    
    return dfs(0, 0, numbers, target);
}

function dfs(sum, count, numbers, target) {
    // 모든 숫자를 사용한 경우
    if (count === numbers.length) {
        return sum === target ? 1 : 0;
    } else {
        // 현재 숫자를 더한 경우와 뺀 경우를 각각 탐색
        return dfs(sum + numbers[count], count + 1, numbers, target) +
               dfs(sum - numbers[count], count + 1, numbers, target);
    }
}