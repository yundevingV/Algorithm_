function solution(prices) {
    var answer = [];
    let stack = []
    let count = 0

    for(let i = 0;i<prices.length-1;i++){
        count = 0
        stack.push(prices[i])
        for(let j = i+1;j<prices.length;j++){
            
            if(stack[stack.length-1] > prices[j]){
                count += 1
                break
            }
            else {
                count += 1
            }
        }
        answer.push(count)
    }
    answer.push(0)

    return answer;
}