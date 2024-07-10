function solution(numbers, target) {
    var answer = 0;

    const dfs = (current_sum, idx) => {
        if (idx === numbers.length) {
            if (current_sum === target) {
                answer += 1;
            }
            return;
        }

        // 현재 요소를 더하는 경우
        dfs(current_sum + numbers[idx], idx + 1);
        // 현재 요소를 빼는 경우
        dfs(current_sum - numbers[idx], idx + 1);
    }

    dfs(0, 0);
    return answer;
}