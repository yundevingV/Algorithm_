function solution(prices) {
    var answer = [];
    let stack = [];
    
    const len = prices.length;
    
    for(let i=0; i<len - 1; i++){
        
        let count = 0;
        stack.push(prices[i]);
        
        for(let j=i+1; j<len; j++){
            if(stack[stack.length - 1] > prices[j]){
                count += 1;
                break;
            }   
            else {
                count += 1;
            }
        }
        answer.push(count);
    }
    answer.push(0);

    return answer;
}