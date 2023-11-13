

function solution(numbers, target) {
    var answer = 0;

    function dfs(n,c){
        if(numbers.length === c){
            if(n === target) {answer += 1;}
            return;
        }
        dfs(n + numbers[c],c+1);
        dfs(n - numbers[c],c+1);
    }
    dfs(0,0);
    
    
    return answer;
}