function solution(s){
    let stack = [];
    
    if(s.length === 0) {
        return false;
    } 
    else {
        for(let i=0;i<s.length;i++){
            // '(' 일때
            if(s[i] === '(') {
                // able                 
                if(stack.length === 0 || stack[stack.length-1] === '(') {
                    stack.push(s[i]);
                }
                // unable
                else if(stack[stack.length-1] === ')') {
                    return false;
                }
            }
            // ')' 일때
            if(s[i] === ')') {
                // able
                if(stack[stack.length-1] === '(') {
                    stack.pop();
                }
                // unable
                else if(stack.length === 0 || stack[stack.length-1] === ')') {
                    return false;
                }
             }
        }
    }
    if(stack.length === 0) return true;
    else return false;
}