function solution(order) {
    var answer = 0;
    let i = 0;
    
    let stack = [];
    
    const len = order.length;
    
    while(answer < len) {
        if (order[answer] > i) {
            i += 1;
            stack.push(i);
        } else if (stack[stack.length - 1] === order[answer]){
            stack.pop();
            answer += 1;            
        } else {
            return answer;
        }
    }
    
    return answer;
}