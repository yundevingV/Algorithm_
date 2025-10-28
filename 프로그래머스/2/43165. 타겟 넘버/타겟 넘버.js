function solution(numbers, target) {
    var answer = 0;
    
    const dfs = (index,currentSum) => {
        if (index === numbers.length) {
            if(currentSum === target) {
                answer ++;
            }
            return;
        }
        dfs(index + 1, currentSum + numbers[index]);
        dfs(index + 1, currentSum - numbers[index]);
    }
    
    dfs(0,0);
    return answer;
}