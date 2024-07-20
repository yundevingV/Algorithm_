function solution(numbers, target) {
    var answer = 0;
    
    const dfs = (numbers,index,sum) =>{
        if(index === numbers.length){
            if(sum === target){
                answer +=1
                return
            }
            else {
                return
            }
        }
        dfs(numbers,index+1,sum+numbers[index])
        dfs(numbers,index+1,sum-numbers[index])
        
    }
    dfs(numbers,0,0)
    return answer;
}